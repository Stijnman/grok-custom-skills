# Testing Guide

This document outlines the testing requirements and best practices for all skills in the **grok-custom-skills** repository.

---

## 📋 Table of Contents

- [Testing Philosophy](#-testing-philosophy)
- [Testing Levels](#-testing-levels)
- [Manual Testing](#-manual-testing)
- [Automated Testing](#-automated-testing)
- [Test Environments](#-test-environments)
- [Test Data Management](#-test-data-management)
- [Skill Category Testing](#-skill-category-testing)
- [CI/CD Pipeline](#-cicd-pipeline)
- [Test Checklists](#-test-checklists)

---

## 🎯 Testing Philosophy

### Core Principles

1. **Safety First**: Never test with production credentials or real user data
2. **Isolation**: Each test should be independent and not affect others
3. **Reproducibility**: Tests should produce consistent results
4. **Coverage**: Test both happy paths and error cases
5. **Documentation**: All tests should be documented and maintainable
6. **Least Privilege**: Tests should use minimum required permissions

### What Must Be Tested

Every skill **MUST** be tested for:
- ✅ Successful workflow execution
- ✅ All error scenarios and edge cases
- ✅ Input validation
- ✅ Rate limiting behavior (where applicable)
- ✅ Authentication and authorization (where applicable)
- ✅ Security considerations
- ✅ Boundary conditions and limitations
- ✅ Human approval requirements (for high-impact actions)

### Quality Gates

Before merging any skill:
- [ ] All manual tests pass
- [ ] Automated tests pass (if applicable)
- [ ] Validation pipeline passes (`scripts/optimize_all_skills.py`)
- [ ] Catalog generation succeeds (`scripts/generate_catalog.py`)
- [ ] No private data detected (`scripts/check_no_private_data.py`)
- [ ] Safety checks pass (`scripts/publish_safety_check.py`)

---

## 🏗️ Testing Levels

### Level 1: Unit Testing (Optional but Recommended)

Test individual functions and components in isolation.

**Example**: Testing input validation functions
```python
# test_input_validation.py
import pytest
from skill_utils import validate_email, validate_trigger

def test_validate_trigger_match():
    """Test that trigger matching works correctly"""
    assert validate_trigger("research web information", "research") == True
    assert validate_trigger("search online", "research") == True
    assert validate_trigger("find data", "research") == False

def test_validate_trigger_empty():
    """Test empty trigger handling"""
    assert validate_trigger("", "research") == False
    assert validate_trigger("   ", "research") == False
```

### Level 2: Integration Testing (Recommended)

Test the complete flow of a skill from trigger to response.

**Example**: Testing a research skill workflow
```python
# test_research_workflow.py
from research_skill import ResearchWorkflow

def test_research_workflow():
    """Test the complete research workflow"""
    workflow = ResearchWorkflow()
    
    # Test happy path
    result = workflow.execute({
        "query": "AI trends 2026",
        "sources": ["web", "news"],
        "depth": "comprehensive"
    })
    
    assert "results" in result
    assert "sources" in result
    assert "metadata" in result
    assert result["metadata"]["query"] == "AI trends 2026"
```

### Level 3: End-to-End Testing (Required for High-Impact Skills)

Test the complete user experience in a sandbox environment.

**Manual Test Script Template**:
```
1. Start with fresh state (no existing sessions/state)
2. Agent receives trigger: "[Test trigger phrase]"
3. Agent executes skill workflow
4. Agent provides output/response
5. Verify: Expected output is produced
6. Verify: All safety checks were applied
7. Verify: No unexpected side effects
8. Cleanup: Reset state
```

---

## 👤 Manual Testing

### Required Manual Tests

For **every skill**, manually test:

#### Positive Tests (Happy Path)
- [ ] Basic execution with all required inputs
- [ ] Execution with all optional inputs
- [ ] Execution with minimal required inputs only
- [ ] All trigger phrases work correctly
- [ ] Output formatting is correct
- [ ] Cross-references to other skills work

#### Negative Tests (Error Cases)
- [ ] Invalid trigger phrases
- [ ] Invalid input formats
- [ ] Missing required inputs
- [ ] Invalid configuration
- [ ] Rate limit exceeded (if applicable)
- [ ] Network failures (simulated)
- [ ] Platform API errors (simulated)
- [ ] Permission/authorization errors

#### Edge Cases
- [ ] Maximum length inputs
- [ ] Special characters in inputs
- [ ] Unicode characters in inputs
- [ ] Empty optional inputs
- [ ] Concurrent requests (if applicable)
- [ ] Session timeout scenarios
- [ ] Human approval timeouts (for HITL skills)

### Manual Testing Checklist Template

```markdown
# Testing Checklist: [Skill Name]

## Setup
- [ ] Test environment configured
- [ ] Test credentials available (sandbox only)
- [ ] Network connectivity verified
- [ ] Previous test state cleaned up

## Skill Metadata
- [ ] SKILL.md has proper YAML frontmatter
- [ ] Description is clear and accurate
- [ ] Triggers are specific and testable
- [ ] Version is specified
- [ ] Dependencies are documented
- [ ] Boundaries are defined

## Happy Path Tests
- [ ] Test 1: Basic execution
- [ ] Test 2: Full configuration
- [ ] Test 3: Minimal configuration
- [ ] Test 4: All trigger variations
- [ ] Test 5: Cross-skill integration (if applicable)

## Error Handling Tests
- [ ] Invalid trigger: _______________
- [ ] Invalid input: _______________
- [ ] Missing required: _______________
- [ ] API error: _______________
- [ ] Network error: _______________
- [ ] Rate limit: _______________
- [ ] Permission error: _______________

## Security Tests
- [ ] No credentials logged
- [ ] Sensitive data masked in output
- [ ] Input validation works
- [ ] No hardcoded credentials
- [ ] Rate limiting respected
- [ ] Least privilege applied
- [ ] Human approval required for high-impact actions

## Documentation Tests
- [ ] README is clear
- [ ] Examples work as documented
- [ ] Limitations are documented
- [ ] Links are valid
- [ ] Cross-references work

## Cleanup
- [ ] All test data removed
- [ ] All test sessions ended
- [ ] No orphaned resources
- [ ] Environment restored to initial state

## Results
- [ ] All tests passed
- [ ] Issues found: _______________
- [ ] Notes: _____________________
- [ ] Screenshots: _______________
```

---

## 🤖 Automated Testing

### Test File Structure

```
grok-custom-skills/
├── .grok/
│   └── skills/
│       └── [skill-name]/
│           ├── SKILL.md
│           └── tests/
│               ├── __init__.py
│               ├── conftest.py          # Fixtures and setup
│               ├── test_metadata.py     # Frontmatter validation
│               ├── test_triggers.py     # Trigger matching
│               ├── test_workflow.py     # Complete flow tests
│               ├── test_validation.py   # Input validation tests
│               └── test_safety.py       # Safety checks
└── tests/
    ├── test_catalog.py          # Catalog generation tests
    └── test_validation.py        # Repository-wide validation
```

### Example Test File

```python
# .grok/skills/research-web/SKILL.md
---
name: research-web
description: Perform web research from approved sources
version: 1.2.0
triggers: ["research web", "search online", "find information"]
---

# .grok/skills/research-web/tests/test_triggers.py
import pytest
from research_web import match_trigger


@pytest.mark.parametrize("trigger,expected", [
    ("research web information", True),
    ("search online for data", True),
    ("find information about", True),
    ("look up facts", False),
    ("browse internet", False),
])
def test_trigger_matching(trigger, expected):
    """Test that triggers match correctly"""
    assert match_trigger(trigger) == expected


class TestInputValidation:
    """Test all input validation scenarios"""
    
    def test_valid_query(self):
        """Test valid query input"""
        assert validate_query("AI trends 2026") == (True, None)
    
    def test_query_too_short(self):
        """Test query minimum length"""
        result, error = validate_query("ab")
        assert result == False
        assert error == "Query too short (min 10 characters)"
    
    def test_query_too_long(self):
        """Test query maximum length"""
        long_query = "a" * 501
        result, error = validate_query(long_query)
        assert result == False
        assert error == "Query too long (max 500 characters)"
    
    def test_query_special_chars(self):
        """Test query with special characters"""
        assert validate_query("What is AI? 2026!") == (True, None)
```

### Using pytest

Install pytest:
```bash
pip install pytest pytest-mock pytest-cov
```

Run tests:
```bash
# Run all tests
pytest

# Run specific test file
pytest .grok/skills/research-web/tests/

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=.grok/skills/research-web --cov-report=html

# Run specific test
pytest .grok/skills/research-web/tests/test_triggers.py::test_trigger_matching
```

---

## 🌍 Test Environments

### Sandbox Environments

Always use sandbox/test environments for testing:

| Purpose | Environment | Notes |
|---------|-------------|-------|
| Web research | Approved sources only | Use sandbox endpoints where available |
| API testing | Mock servers | Use `unittest.mock` or similar |
| File operations | Temporary directories | Use `tempfile` or `/tmp` |
| Network requests | Local mock servers | Never use production endpoints |

### Test Data

**Never use real data for testing:**
- Use fake emails: `test-123456@example.com`
- Use fake names: `Test User`, `John Doe`
- Use fake organizations: `Test Corp`, `Example Inc`
- Use fake API keys: `test_key_1234567890`

### Environment Variables

Use environment variables for test configuration:

```bash
# .env.test
export TEST_MODE=true
export SANDBOX_ENDPOINT=https://sandbox.example.com
export TEST_API_KEY=test_key_1234567890
```

**Never commit .env files to version control!**

Ensure .gitignore includes:
```
.env
.env.*
*.env
.env.local
```

---

## 🗃️ Test Data Management

### Test Data Principles

1. **Use fake data**: Never use real user data
2. **Clean up**: Delete all test data after tests complete
3. **Isolate**: Each test should use unique data
4. **Anonymize**: Remove any real identifiers
5. **Deterministic**: Tests should produce the same results every time

### Generating Test Data

```python
# utilities/test_data_factory.py
import random
import string
from datetime import datetime


def generate_test_id(length=8):
    """Generate a unique test ID"""
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


def generate_test_email():
    """Generate a unique test email"""
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
    test_id = generate_test_id(6)
    return f"test_{timestamp}_{test_id}@example.com"


def generate_test_query():
    """Generate a test query"""
    topics = ["AI", "machine learning", "automation", "research", "development"]
    years = ["2024", "2025", "2026"]
    return f"{random.choice(topics)} trends {random.choice(years)}"
```

### Test Data Cleanup

Every test file should include cleanup:

```python
# conftest.py
import pytest
import os
import tempfile


@pytest.fixture(scope="session")
def cleanup():
    """Clean up all test data after session"""
    yield
    # Clean up test files
    cleanup_test_files()
    # Clean up test directories
    cleanup_test_dirs()
    # Clean up environment
    cleanup_test_env()


def cleanup_test_files():
    """Delete all test files created during testing"""
    for filepath in TEST_FILES:
        if os.path.exists(filepath):
            os.remove(filepath)


def cleanup_test_dirs():
    """Delete all test directories created during testing"""
    for dirpath in TEST_DIRS:
        if os.path.exists(dirpath):
            import shutil
            shutil.rmtree(dirpath)


def cleanup_test_env():
    """Clean up test environment variables"""
    for var in TEST_ENV_VARS:
        if var in os.environ:
            del os.environ[var]
```

---

## 🎯 Skill Category Testing

### Workflow & Orchestration Skills

Test multi-step workflows, agent coordination, and failure handling.

**Focus Areas**:
- Agent handoffs work correctly
- State is maintained across steps
- Failures are handled gracefully
- Rollback works (if applicable)
- Progress is tracked

### Skill Development & Operations Skills

Test skill creation, auditing, evolution, testing, and comparison.

**Focus Areas**:
- Skills can be created programmatically
- Audit checks work
- Evolution preserves data
- Comparison is accurate
- Testing is comprehensive

### Safety, Privacy & Governance Skills

Test human approval, data redaction, MCP auditing, and responsible browsing.

**Focus Areas**:
- Human approval is required for high-impact actions
- Data is redacted correctly
- MCP exposure is audited
- Browsing is responsible and safe
- Privacy controls work

### Research, Web & Integrations Skills

Test source-aware research, repository inspection, tool discovery, and service connections.

**Focus Areas**:
- Sources are respected
- Repository inspection works
- Tool discovery is accurate
- Service connections are secure
- Rate limiting is respected

### Memory, Context & Knowledge Skills

Test context budgets, structured knowledge, semantic memory, and session handoffs.

**Focus Areas**:
- Context budgets are respected
- Knowledge is structured correctly
- Semantic memory works
- Session handoffs preserve context
- Memory limits are enforced

### Media, Voice & Visual Work Skills

Test image generation, video analysis, voice processing, and song-writing prompts.

**Focus Areas**:
- Images can be generated
- Video analysis works
- Voice processing works
- Prompts are safe and appropriate
- Output quality is acceptable

### Messaging & Navigation Skills

Test message assessment, safe responses, traffic information, and route information.

**Focus Areas**:
- Messages are assessed correctly
- Responses are safe
- Traffic information is accurate
- Route information is accurate
- Privacy is maintained

---

## ⚙️ CI/CD Pipeline

### GitHub Actions Workflow

The repository includes a validation workflow (`.github/workflows/validate.yml`) that runs on:
- Pull requests to main
- Pushes to main
- Changes to skills, scripts, or validation files

**Workflow Steps**:
1. Check out repository
2. Set up Python
3. Run repository validation pipeline (`scripts/optimize_all_skills.py`)
4. Run catalog regression tests
5. Confirm formatting and generated catalog are current

### Enhanced CI/CD (Recommended)

For comprehensive testing, consider adding:

```yaml
# .github/workflows/test.yml
name: Test Skills

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  validate:
    name: Validate
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: python3 scripts/optimize_all_skills.py
      - run: python3 -m unittest discover -s tests -p "test_*.py"
      - run: git diff --check
      - run: git diff --exit-code -- SKILLS_INDEX.md

  test:
    name: Run Tests
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: pip install pytest pytest-mock pytest-cov
      - run: pytest tests/ -v --tb=short --cov=tests --cov-report=xml

  lint:
    name: Lint Documentation
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install markdown-lint
      - run: find .grok/skills -name "SKILL.md" -exec markdown-lint {} \;

  security:
    name: Security Scan
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: python3 scripts/check_no_private_data.py
      - run: python3 scripts/publish_safety_check.py
```

---

## ✅ Test Checklists

### New Skill Checklist

Before adding a new skill to the repository:

- [ ] Manual testing completed for all flows
- [ ] All error cases tested
- [ ] Input validation implemented and tested
- [ ] Rate limiting verified (if applicable)
- [ ] Security considerations documented
- [ ] Usage examples included and tested
- [ ] Testing checklist in SKILL.md
- [ ] Cross-references work
- [ ] All links are valid
- [ ] No hardcoded credentials
- [ ] Metadata is complete
- [ ] Triggers are specific
- [ ] Boundaries are defined
- [ ] Validation pipeline passes
- [ ] Catalog generation succeeds

### Existing Skill Update Checklist

Before updating an existing skill:

- [ ] Changes tested with existing functionality
- [ ] No breaking changes (or documented if breaking)
- [ ] Version bumped appropriately
- [ ] Changelog updated
- [ ] New tests added for new functionality
- [ ] Existing tests still pass
- [ ] Documentation updated
- [ ] Validation pipeline passes
- [ ] Catalog generation succeeds

### Pre-PR Checklist

Before opening a pull request:

- [ ] All manual tests pass
- [ ] Automated tests pass (if applicable)
- [ ] Code follows repository standards
- [ ] Documentation is complete
- [ ] No sensitive data committed
- [ ] Version numbers updated
- [ ] Testing checklist completed
- [ ] Pre-commit hooks pass
- [ ] Linting passes
- [ ] Security checks pass

### Pre-Release Checklist

Before creating a release:

- [ ] All tests pass in CI
- [ ] All PRs merged
- [ ] CHANGELOG.md updated
- [ ] Version numbers updated
- [ ] Security review completed
- [ ] All skills tested end-to-end
- [ ] Breaking changes documented
- [ ] Migration guide written (if needed)
- [ ] SKILLS_INDEX.md regenerated
- [ ] Validation pipeline passes

---

## 📊 Test Coverage Reports

Generate coverage reports to identify untested areas:

```bash
# Install coverage
pip install pytest-cov

# Run tests with coverage for a specific skill
pytest .grok/skills/[skill-name]/tests/ --cov=.grok/skills/[skill-name] --cov-report=html

# Open coverage report
open htmlcov/index.html

# Run all tests with coverage
pytest tests/ --cov=tests --cov-report=html
```

Aim for **80%+ coverage** for production skills.

---

## 🛠️ Test Utilities

### Mock Server

For testing API interactions without hitting real services:

```python
# tests/conftest.py
import pytest
from unittest.mock import Mock, patch
import requests


@pytest.fixture
def mock_requests():
    """Mock requests library for API testing"""
    with patch('requests.get') as mock_get, \
         patch('requests.post') as mock_post, \
         patch('requests.put') as mock_put, \
         patch('requests.delete') as mock_delete:
        
        mock_get.return_value = Mock()
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {}
        
        mock_post.return_value = Mock()
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {}
        
        mock_put.return_value = Mock()
        mock_put.return_value.status_code = 200
        
        mock_delete.return_value = Mock()
        mock_delete.return_value.status_code = 200
        
        yield mock_get, mock_post, mock_put, mock_delete
```

### Test Data Factories

```python
# tests/factories.py
import factory
from datetime import datetime


class SkillFactory(factory.Factory):
    class Meta:
        model = dict
    
    name = factory.Faker("word")
    description = factory.Faker("sentence")
    version = "1.0.0"
    triggers = factory.LazyAttribute(lambda o: [f"{o.name} action", f"do {o.name}"])


class UserFactory(factory.Factory):
    class Meta:
        model = dict
    
    name = factory.Faker("name")
    email = factory.LazyAttribute(
        lambda o: f"test_{datetime.now().strftime('%Y%m%d%H%M%S%f')[:14]}@example.com"
    )
    company = factory.Faker("company")


# Usage
skill = SkillFactory()
user = UserFactory()
```

---

## 🎯 Summary

| Aspect | Requirement |
|--------|-------------|
| Manual Testing | ✅ Required for all skills |
| Automated Testing | ⚠️ Recommended for all skills |
| Test Coverage | ≥ 80% for production skills |
| Test Environment | Sandbox only, never production |
| Test Data | Fake data only, cleaned up after |
| Validation | ✅ Required for all PRs |
| CI/CD | ✅ Required for all PRs |

**Remember**: The quality of your tests directly impacts the reliability and safety of the skills in production use.

---

## 📚 Additional Resources

- [PUBLISHING.md](./PUBLISHING.md) - Publishing checklist and requirements
- [SECURITY.md](./SECURITY.md) - Security policy and requirements
- [CONTRIBUTING.md](./CONTRIBUTING.md) - Contribution guidelines
- [SKILLS_INDEX.md](./SKILLS_INDEX.md) - Complete skills catalog

---

*Last updated: September 11, 2026*
*Maintainer: Stijnman*
