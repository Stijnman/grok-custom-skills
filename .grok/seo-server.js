const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const fs = require('fs');
const path = require('path');

const PORT = process.env.PORT || 3000;
const NODE_ENV = process.env.NODE_ENV || 'development';
const MAX_REQUESTS_PER_MINUTE = NODE_ENV === 'production' ? 100 : 1000;

const app = express();

app.use(helmet());
app.use(cors({
  origin: process.env.ALLOWED_ORIGINS ? process.env.ALLOWED_ORIGINS.split(',') : '*',
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization']
}));

const limiter = rateLimit({
  windowMs: 60 * 1000,
  max: MAX_REQUESTS_PER_MINUTE,
  message: { error: 'Too many requests, please try again later.', status: 429 },
  standardHeaders: true,
  legacyHeaders: false
});

app.use(limiter);
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true, limit: '10mb' }));

app.use((req, res, next) => {
  const start = Date.now();
  res.on('finish', () => {
    const duration = Date.now() - start;
    console.log(`${new Date().toISOString()} - ${req.method} ${req.originalUrl} - ${res.statusCode} - ${duration}ms`);
  });
  next();
});

app.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    timestamp: new Date().toISOString(),
    version: '1.0.0',
    environment: NODE_ENV
  });
});

app.get('/api/info', (req, res) => {
  const packageJson = require('./package.json');
  res.json({
    name: packageJson.name,
    version: packageJson.version,
    description: packageJson.description,
    author: packageJson.author,
    endpoints: {
      health: '/health',
      info: '/api/info',
      skills: '/api/skills',
      skillsDetail: '/api/skills/:id',
      seo: '/api/seo/*',
      geo: '/api/geo/*',
      backlinko: '/api/backlinko/*'
    },
    environment: NODE_ENV
  });
});

const SKILLS_DIR = path.join(__dirname, 'skills');

function loadSkills() {
  try {
    const files = fs.readdirSync(SKILLS_DIR);
    const skills = [];
    
    files.forEach(file => {
      if (file.endsWith('.json')) {
        const skillPath = path.join(SKILLS_DIR, file);
        const skillData = JSON.parse(fs.readFileSync(skillPath, 'utf8'));
        skills.push(skillData);
      }
    });
    
    return skills;
  } catch (error) {
    console.error('Error loading skills:', error);
    return [];
  }
}

function getSkillById(skills, id) {
  return skills.find(skill => skill.id === id);
}

app.get('/api/skills', (req, res) => {
  try {
    const skills = loadSkills();
    res.json({
      count: skills.length,
      skills: skills.map(skill => ({
        id: skill.id,
        name: skill.name,
        description: skill.description,
        version: skill.version,
        category: skill.category,
        tags: skill.tags
      }))
    });
  } catch (error) {
    res.status(500).json({ error: 'Failed to load skills', details: error.message });
  }
});

app.get('/api/skills/:id', (req, res) => {
  try {
    const skills = loadSkills();
    const skill = getSkillById(skills, req.params.id);
    
    if (!skill) {
      return res.status(404).json({ error: 'Skill not found', id: req.params.id });
    }
    
    res.json(skill);
  } catch (error) {
    res.status(500).json({ error: 'Failed to load skill', details: error.message });
  }
});

app.use((err, req, res, next) => {
  console.error('Error:', err);
  res.status(err.status || 500).json({
    error: err.message || 'Internal Server Error',
    ...(NODE_ENV === 'development' && { stack: err.stack })
  });
});

app.use((req, res) => {
  res.status(404).json({ error: 'Not Found', path: req.originalUrl });
});

const server = app.listen(PORT, () => {
  console.log(`SEO/GEO Intelligence Server running on port ${PORT}`);
  console.log(`Environment: ${NODE_ENV}`);
  console.log(`Health check: http://localhost:${PORT}/health`);
  console.log(`API info: http://localhost:${PORT}/api/info`);
});

process.on('SIGTERM', () => {
  console.log('SIGTERM received. Shutting down gracefully...');
  server.close(() => {
    console.log('Server closed.');
    process.exit(0);
  });
});

process.on('SIGINT', () => {
  console.log('SIGINT received. Shutting down gracefully...');
  server.close(() => {
    console.log('Server closed.');
    process.exit(0);
  });
});

module.exports = app;
