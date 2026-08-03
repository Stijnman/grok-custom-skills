#!/bin/bash

# Create all 12 SEO & GEO Intelligence Skill files

# Create skills directory
mkdir -p skills

# 1. SEO Analyzer
cat > skills/seo-analyzer.json << 'EOF'
{
  "name": "SEO Analyzer",
  "id": "seo-analyzer",
  "description": "Comprehensive SEO analysis with keyword research, competition analysis, and ranking tracking",
  "version": "1.0.0",
  "author": "Stijnman",
  "category": "SEO",
  "tags": ["seo", "analysis", "keywords", "ranking", "competition"],
  "capabilities": ["keyword_research", "competitor_analysis", "ranking_tracking", "backlink_analysis", "technical_seo_audit", "content_optimization"],
  "tools": [
    {"name": "analyze_keywords", "description": "Perform comprehensive keyword research and analysis", "parameters": {"keywords": "array", "search_volume_min": "number", "competition_max": "number", "location": "string"}},
    {"name": "analyze_competitors", "description": "Analyze competitor websites and SEO strategies", "parameters": {"competitors": "array", "depth": "string", "focus_areas": "array"}},
    {"name": "track_rankings", "description": "Track keyword rankings across search engines", "parameters": {"keywords": "array", "domains": "array", "search_engines": "array", "frequency": "string"}}
  ],
  "dependencies": ["fetch_engine", "seo_database"],
  "configuration": {"api_keys": {"google_search_console": "", "ahrefs": "", "moz": "", "semrush": ""}, "search_engines": ["google", "bing", "yahoo"], "default_location": "us"}
}
EOF

# 2. Backlink Monitor
cat > skills/backlink-monitor.json << 'EOF'
{
  "name": "Backlink Monitor",
  "id": "backlink-monitor",
  "description": "Monitor and analyze backlinks for SEO performance and link building opportunities",
  "version": "1.0.0",
  "author": "Stijnman",
  "category": "SEO",
  "tags": ["backlinks", "link-building", "seo", "monitoring", "analysis"],
  "capabilities": ["backlink_discovery", "link_quality_analysis", "toxic_link_detection", "link_building_opportunities", "anchor_text_analysis", "referring_domains_tracking"],
  "tools": [
    {"name": "discover_backlinks", "description": "Discover all backlinks pointing to a domain", "parameters": {"domain": "string", "include_subdomains": "boolean", "limit": "number"}},
    {"name": "analyze_link_quality", "description": "Analyze the quality and authority of backlinks", "parameters": {"backlinks": "array", "metrics": "array"}},
    {"name": "detect_toxic_links", "description": "Identify potentially harmful or toxic backlinks", "parameters": {"backlinks": "array", "threshold": "number"}}
  ],
  "dependencies": ["fetch_engine", "seo_database"],
  "configuration": {"api_keys": {"ahrefs": "", "majestic": "", "moz": ""}, "quality_thresholds": {"domain_authority_min": 20, "spam_score_max": 5, "trust_flow_min": 10}}
}
EOF

# 3. Content Optimizer
cat > skills/content-optimizer.json << 'EOF'
{
  "name": "Content Optimizer",
  "id": "content-optimizer",
  "description": "Optimize content for SEO with keyword density, readability, and semantic analysis",
  "version": "1.0.0",
  "author": "Stijnman",
  "category": "SEO",
  "tags": ["content", "seo", "optimization", "keywords", "readability"],
  "capabilities": ["keyword_density_analysis", "content_gap_analysis", "readability_scoring", "semantic_analysis", "content_suggestions", "meta_tag_optimization"],
  "tools": [
    {"name": "analyze_content", "description": "Analyze content for SEO optimization opportunities", "parameters": {"content": "string", "target_keywords": "array", "language": "string"}},
    {"name": "generate_optimized_content", "description": "Generate SEO-optimized content based on analysis", "parameters": {"topic": "string", "target_keywords": "array", "content_type": "string", "length": "number"}},
    {"name": "optimize_meta_tags", "description": "Generate optimized meta tags for content", "parameters": {"title": "string", "description": "string", "keywords": "array", "url": "string"}}
  ],
  "dependencies": ["nlp_engine", "seo_database"],
  "configuration": {"keyword_density": {"min": 0.5, "max": 3.0}, "readability_targets": {"flesch_reading_ease_min": 60, "grade_level_max": 12}}
}
EOF

# 4. Technical SEO Auditor
cat > skills/technical-seo-auditor.json << 'EOF'
{
  "name": "Technical SEO Auditor",
  "id": "technical-seo-auditor",
  "description": "Comprehensive technical SEO auditing for website performance and crawlability",
  "version": "1.0.0",
  "author": "Stijnman",
  "category": "SEO",
  "tags": ["technical-seo", "audit", "crawlability", "performance", "website"],
  "capabilities": ["site_crawling", "indexability_analysis", "page_speed_analysis", "mobile_friendliness", "structured_data_validation", "canonical_tag_analysis", "redirect_chain_analysis", "broken_link_detection"],
  "tools": [
    {"name": "crawl_website", "description": "Crawl website to identify technical SEO issues", "parameters": {"url": "string", "max_pages": "number", "depth": "number", "user_agent": "string"}},
    {"name": "analyze_page_speed", "description": "Analyze page loading speed and performance metrics", "parameters": {"url": "string", "device": "string", "location": "string"}},
    {"name": "validate_structured_data", "description": "Validate and test structured data markup", "parameters": {"url": "string", "schema_types": "array"}}
  ],
  "dependencies": ["fetch_engine", "browser_automation"],
  "configuration": {"crawl_settings": {"max_concurrent_requests": 5, "request_timeout": 30, "respect_robots_txt": true}, "performance_thresholds": {"lighthouse_score_min": 80, "page_load_time_max": 3.0, "mobile_friendly": true}}
}
EOF

# 5. GEO Location Analyzer
cat > skills/geo-location-analyzer.json << 'EOF'
{
  "name": "GEO Location Analyzer",
  "id": "geo-location-analyzer",
  "description": "Analyze geographic locations, coordinates, and spatial data for intelligence gathering",
  "version": "1.0.0",
  "author": "Stijnman",
  "category": "GEO Intelligence",
  "tags": ["geo", "location", "gps", "spatial", "mapping", "intelligence"],
  "capabilities": ["coordinate_geocoding", "reverse_geocoding", "distance_calculation", "location_intelligence", "geofencing", "spatial_analysis", "elevation_data", "timezone_lookup"],
  "tools": [
    {"name": "geocode_address", "description": "Convert address to geographic coordinates", "parameters": {"address": "string", "country": "string", "precision": "string"}},
    {"name": "reverse_geocode", "description": "Convert coordinates to human-readable address", "parameters": {"latitude": "number", "longitude": "number", "language": "string"}},
    {"name": "calculate_distance", "description": "Calculate distance between two geographic points", "parameters": {"point_a": "object", "point_b": "object", "unit": "string"}},
    {"name": "analyze_location_intelligence", "description": "Gather intelligence about a specific geographic location", "parameters": {"location": "object", "radius_km": "number", "data_types": "array"}}
  ],
  "dependencies": ["geo_database", "mapping_service"],
  "configuration": {"api_keys": {"google_maps": "", "openstreetmap": "", "here_maps": "", "mapbox": ""}, "default_providers": ["google", "openstreetmap"], "distance_units": "metric"}
}
EOF

# 6. GEO IP Intelligence
cat > skills/geo-ip-intelligence.json << 'EOF'
{
  "name": "GEO IP Intelligence",
  "id": "geo-ip-intelligence",
  "description": "IP address geolocation, network analysis, and threat intelligence",
  "version": "1.0.0",
  "author": "Stijnman",
  "category": "GEO Intelligence",
  "tags": ["geo", "ip", "geolocation", "network", "threat-intelligence", "cybersecurity"],
  "capabilities": ["ip_geolocation", "network_analysis", "threat_intelligence", "proxy_vpn_detection", "asn_lookup", "ip_reputation", "bulk_ip_analysis", "geographic_distribution"],
  "tools": [
    {"name": "lookup_ip", "description": "Get comprehensive information about an IP address", "parameters": {"ip_address": "string", "include_threat_data": "boolean", "include_network_data": "boolean"}},
    {"name": "analyze_ip_batch", "description": "Analyze multiple IP addresses in batch", "parameters": {"ip_addresses": "array", "fields": "array"}},
    {"name": "detect_proxy_vpn", "description": "Detect if IP address is using proxy, VPN, or Tor", "parameters": {"ip_address": "string", "confidence_threshold": "number"}},
    {"name": "get_geographic_distribution", "description": "Get geographic distribution of IP addresses", "parameters": {"ip_addresses": "array", "group_by": "string"}}
  ],
  "dependencies": ["ip_database", "threat_intelligence_api"],
  "configuration": {"api_keys": {"ipinfo": "", "ip2location": "", "maxmind": "", "abuseipdb": "", "shodan": ""}, "threat_detection": {"enable_proxy_detection": true, "enable_vpn_detection": true, "enable_tor_detection": true, "risk_threshold": 70}}
}
EOF

# 7. GEO Market Intelligence
cat > skills/geo-market-intelligence.json << 'EOF'
{
  "name": "GEO Market Intelligence",
  "id": "geo-market-intelligence",
  "description": "Market analysis by geographic region, demographic insights, and economic data",
  "version": "1.0.0",
  "author": "Stijnman",
  "category": "GEO Intelligence",
  "tags": ["geo", "market", "demographics", "economic", "business-intelligence", "regional-analysis"],
  "capabilities": ["regional_market_analysis", "demographic_insights", "economic_data", "competitive_landscape", "consumer_behavior", "market_trends", "regulatory_environment", "cultural_analysis"],
  "tools": [
    {"name": "analyze_regional_market", "description": "Analyze market potential for a specific geographic region", "parameters": {"region": "object", "industry": "string", "time_period": "string", "metrics": "array"}},
    {"name": "get_demographic_data", "description": "Get demographic information for a geographic area", "parameters": {"location": "object", "demographic_types": "array", "age_ranges": "array", "income_levels": "array"}},
    {"name": "analyze_economic_indicators", "description": "Analyze economic indicators for a region", "parameters": {"region": "object", "indicators": "array", "time_range": "object"}},
    {"name": "compare_regions", "description": "Compare multiple geographic regions across various metrics", "parameters": {"regions": "array", "comparison_metrics": "array", "normalization": "string"}}
  ],
  "dependencies": ["market_data_api", "demographic_database"],
  "configuration": {"api_keys": {"census_bureau": "", "world_bank": "", "statista": "", "nielsen": "", "ibisworld": ""}, "data_sources": ["government", "commercial", "open_data"], "currency": "USD"}
}
EOF

# 8. GEO Social Media Intelligence
cat > skills/geo-social-media-intelligence.json << 'EOF'
{
  "name": "GEO Social Media Intelligence",
  "id": "geo-social-media-intelligence",
  "description": "Social media analysis by geographic location, trends, and influencer mapping",
  "version": "1.0.0",
  "author": "Stijnman",
  "category": "GEO Intelligence",
  "tags": ["geo", "social-media", "trends", "influencers", "sentiment", "engagement"],
  "capabilities": ["geographic_social_analysis", "trend_mapping", "influencer_identification", "sentiment_analysis", "engagement_metrics", "hashtag_analysis", "competitive_social_analysis", "crisis_detection"],
  "tools": [
    {"name": "analyze_social_by_location", "description": "Analyze social media activity by geographic location", "parameters": {"location": "object", "platforms": "array", "keywords": "array", "time_range": "object", "sentiment_analysis": "boolean"}},
    {"name": "identify_influencers", "description": "Identify social media influencers in a geographic area", "parameters": {"location": "object", "industry": "string", "min_followers": "number", "engagement_rate_min": "number", "platforms": "array"}},
    {"name": "track_social_trends", "description": "Track social media trends by geographic region", "parameters": {"regions": "array", "keywords": "array", "platforms": "array", "time_range": "object", "trend_type": "string"}},
    {"name": "analyze_sentiment_by_location", "description": "Analyze sentiment of social media posts by location", "parameters": {"location": "object", "keywords": "array", "platforms": "array", "time_range": "object", "sentiment_granularity": "string"}}
  ],
  "dependencies": ["social_media_api", "nlp_engine"],
  "configuration": {"api_keys": {"twitter_api": "", "facebook_graph": "", "instagram_basic": "", "linkedin_api": "", "reddit_api": "", "tiktok_api": ""}, "rate_limits": {"requests_per_minute": 100, "requests_per_day": 10000}, "data_retention_days": 90}
}
EOF

# 9. Backlinko Keyword Research
cat > skills/backlinko-keyword-research.json << 'EOF'
{
  "name": "Backlinko Keyword Research",
  "id": "backlinko-keyword-research",
  "description": "Advanced keyword research using Backlinko methodology and proven SEO strategies",
  "version": "1.0.0",
  "author": "Stijnman",
  "category": "SEO",
  "tags": ["backlinko", "keyword-research", "seo", "brian-dean", "advanced-seo"],
  "capabilities": ["long_tail_keyword_discovery", "competitor_keyword_gap_analysis", "search_intent_analysis", "keyword_difficulty_scoring", "serp_feature_analysis", "content_angle_identification", "keyword_clustering", "seasonal_trend_analysis"],
  "tools": [
    {"name": "find_long_tail_keywords", "description": "Discover long-tail keywords with high potential using Backlinko methodology", "parameters": {"seed_keywords": "array", "search_volume_min": "number", "keyword_difficulty_max": "number", "include_questions": "boolean", "include_comparisons": "boolean"}},
    {"name": "analyze_competitor_keywords", "description": "Analyze competitor keywords using Backlinko's proven strategies", "parameters": {"competitors": "array", "exclude_branded": "boolean", "filter_by_intent": "array", "min_traffic": "number"}},
    {"name": "identify_content_angles", "description": "Identify winning content angles based on Backlinko's skyscraper technique", "parameters": {"topic": "string", "competitor_urls": "array", "content_types": "array"}},
    {"name": "score_keyword_difficulty", "description": "Score keyword difficulty using Backlinko's proprietary methodology", "parameters": {"keywords": "array", "include_serp_analysis": "boolean", "competitive_analysis": "boolean"}}
  ],
  "dependencies": ["fetch_engine", "seo_database", "backlinko_api"],
  "configuration": {"backlinko_settings": {"use_skyscraper_technique": true, "prioritize_long_tail": true, "minimum_content_length": 1500, "target_backlinks_per_page": 10}, "difficulty_thresholds": {"easy_max": 30, "medium_max": 60, "hard_min": 61}}
}
EOF

# 10. Backlinko Content Strategy
cat > skills/backlinko-content-strategy.json << 'EOF'
{
  "name": "Backlinko Content Strategy",
  "id": "backlinko-content-strategy",
  "description": "Content strategy and creation using Backlinko's proven frameworks and templates",
  "version": "1.0.0",
  "author": "Stijnman",
  "category": "SEO",
  "tags": ["backlinko", "content-strategy", "seo", "content-creation", "brian-dean"],
  "capabilities": ["content_brief_creation", "content_outline_generation", "content_optimization", "content_promotion_strategy", "content_audit", "content_upgrade_recommendations", "content_calendar_creation", "content_performance_tracking"],
  "tools": [
    {"name": "create_content_brief", "description": "Create comprehensive content briefs using Backlinko methodology", "parameters": {"topic": "string", "target_keywords": "array", "competitor_urls": "array", "content_type": "string", "target_audience": "string"}},
    {"name": "generate_content_outline", "description": "Generate SEO-optimized content outlines using Backlinko frameworks", "parameters": {"topic": "string", "content_type": "string", "target_keywords": "array", "include_faq": "boolean", "include_statistics": "boolean"}},
    {"name": "optimize_existing_content", "description": "Optimize existing content using Backlinko's proven techniques", "parameters": {"content": "string", "url": "string", "target_keywords": "array", "competitor_urls": "array"}},
    {"name": "create_promotion_strategy", "description": "Create content promotion strategy using Backlinko's outreach methods", "parameters": {"content_url": "string", "target_audience": "string", "promotion_channels": "array", "budget": "number"}}
  ],
  "dependencies": ["nlp_engine", "seo_database", "content_analyzer"],
  "configuration": {"backlinko_frameworks": {"use_skyscraper_technique": true, "use_step_by_step_guide": true, "use_ultimate_guide": true, "use_case_study_approach": true}, "content_standards": {"minimum_word_count": 1500, "target_readability_score": 70, "include_visuals": true, "internal_linking_target": 5}}
}
EOF

# 11. Backlinko Link Building
cat > skills/backlinko-link-building.json << 'EOF'
{
  "name": "Backlinko Link Building",
  "id": "backlinko-link-building",
  "description": "Link building strategies and outreach using Backlinko's proven methods",
  "version": "1.0.0",
  "author": "Stijnman",
  "category": "SEO",
  "tags": ["backlinko", "link-building", "seo", "outreach", "brian-dean", "white-hat-seo"],
  "capabilities": ["link_prospect_discovery", "outreach_strategy", "guest_posting_opportunities", "broken_link_building", "skyscraper_technique", "resource_page_link_building", "expert_roundup_creation", "link_reclamation"],
  "tools": [
    {"name": "find_link_prospects", "description": "Find high-quality link building prospects using Backlinko methodology", "parameters": {"target_keywords": "array", "industry": "string", "prospect_types": "array", "domain_authority_min": "number", "limit": "number"}},
    {"name": "create_outreach_strategy", "description": "Create personalized outreach strategy using Backlinko's proven templates", "parameters": {"prospects": "array", "outreach_type": "string", "value_proposition": "string", "follow_up_sequence": "boolean"}},
    {"name": "execute_skyscraper_technique", "description": "Execute the skyscraper technique for link building", "parameters": {"target_keywords": "array", "competitor_urls": "array", "content_quality": "string", "outreach_scale": "string"}},
    {"name": "find_broken_link_opportunities", "description": "Find broken link building opportunities", "parameters": {"target_sites": "array", "industry_keywords": "array", "replacement_content": "string"}}
  ],
  "dependencies": ["fetch_engine", "email_outreach", "seo_database"],
  "configuration": {"backlinko_methods": {"skyscraper_technique_enabled": true, "guest_posting_enabled": true, "broken_link_building_enabled": true, "resource_page_building_enabled": true}, "outreach_settings": {"personalization_level": "high", "follow_up_count": 3, "response_rate_target": 0.15}, "quality_thresholds": {"domain_authority_min": 20, "spam_score_max": 5, "relevance_score_min": 70}}
}
EOF

# 12. Backlinko SEO Audit
cat > skills/backlinko-seo-audit.json << 'EOF'
{
  "name": "Backlinko SEO Audit",
  "id": "backlinko-seo-audit",
  "description": "Comprehensive SEO audit using Backlinko's proven checklist and methodology",
  "version": "1.0.0",
  "author": "Stijnman",
  "category": "SEO",
  "tags": ["backlinko", "seo-audit", "website-audit", "brian-dean", "technical-seo"],
  "capabilities": ["comprehensive_seo_audit", "technical_seo_analysis", "on_page_seo_analysis", "off_page_seo_analysis", "content_audit", "backlink_profile_analysis", "competitive_analysis", "actionable_recommendations"],
  "tools": [
    {"name": "perform_full_seo_audit", "description": "Perform comprehensive SEO audit using Backlinko's 200+ point checklist", "parameters": {"url": "string", "include_competitor_analysis": "boolean", "depth": "string", "focus_areas": "array"}},
    {"name": "analyze_technical_seo", "description": "Analyze technical SEO factors using Backlinko methodology", "parameters": {"url": "string", "check_crawlability": "boolean", "check_indexability": "boolean", "check_site_speed": "boolean", "check_mobile_friendliness": "boolean"}},
    {"name": "analyze_on_page_seo", "description": "Analyze on-page SEO factors", "parameters": {"url": "string", "target_keywords": "array", "check_content_quality": "boolean", "check_keyword_optimization": "boolean", "check_internal_linking": "boolean"}},
    {"name": "generate_audit_report", "description": "Generate comprehensive SEO audit report with actionable recommendations", "parameters": {"audit_data": "object", "format": "string", "include_priority_scoring": "boolean", "include_implementation_guide": "boolean"}}
  ],
  "dependencies": ["fetch_engine", "seo_database", "browser_automation"],
  "configuration": {"audit_settings": {"check_all_pages": false, "max_pages_to_audit": 50, "include_screenshots": true, "generate_pdf_report": true}, "scoring_weights": {"technical_seo_weight": 0.3, "on_page_seo_weight": 0.25, "content_quality_weight": 0.2, "backlink_profile_weight": 0.15, "user_experience_weight": 0.1}}
}
EOF

echo -e "${GREEN}✓ All 12 SEO & GEO Intelligence skills created successfully!${NC}"
