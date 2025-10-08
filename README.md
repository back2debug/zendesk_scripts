# Zendesk Support Engineering Scripts

> **Archive Notice**: This repository contains legacy scripts from 2017-2018 used for managing a Zendesk Help Center and performing lightweight analytics. The company was acquired and the Help Center is no longer active. These scripts are preserved for reference and educational purposes.

## Overview

This collection of scripts was developed during my time as a Support Engineer to automate Help Center management tasks and extract analytics from Zendesk. The tools helped streamline article management, ticket analysis, and Help Center customization.

## Repository Structure

### Data Extraction Scripts (Python & Shell)

**Article Management:**
- `curl_articles.sh` - Shell script to fetch articles via Zendesk API
- `get_active_articles.py` - Python script to retrieve all active/published articles from the Help Center

**Ticket Management:**
- `curl_tickets.sh` - Shell script to fetch ticket data via API
- `get_zendesk_tickets.py` - Python script for comprehensive ticket retrieval
- `incremental_ticket_list.py` - Python script to fetch tickets incrementally (useful for regular updates)
- `ticktets_to_excel_file.py` - Python script to export ticket data to Excel format for analysis

**Macro Management:**
- `get_active_macros.py` - Python script to retrieves active Zendesk macros for documentation or backup

### Help Center Customization Files

**Visual Customizations (CSS):**
- `helpcenter_hover_categories.css` - Category hover effects for improved UX
- `helpcenter_status_update_color.css` - Custom color schemes for status indicators

**Interactive Features (HTML/JavaScript):**
- `helpcenter_footer_icons.html` - Custom footer with icon links
- `helpcenter_images_for_categories.html` - Category page image displays
- `helpcenter_status_widget.html` - Status indicator widget for system status
- `helpcenter_status_widget.js` - JavaScript functionality for status widget
- `no_author_zendesk_article.js` - Hides author information from articles

### Documentation
- `no_email_payload.md` - Documentation to update webhook trigger configurations

## Prerequisites

### For Python Scripts (check the import section of scripts for other pre-reqs):
```bash
pip install requests
```

## Configuration

Most scripts require Zendesk API credentials. Typically configured via:
- Environment variables (`ZENDESK_SUBDOMAIN`, `ZENDESK_EMAIL`, `ZENDESK_API_TOKEN`)
- Or hardcoded in script (remember to update before use and not commit the tokens!)

Example setup:
```bash
export ZENDESK_SUBDOMAIN="yourcompany"
export ZENDESK_EMAIL="your.email@company.com"
export ZENDESK_API_TOKEN="your_api_token_here"
```

## Usage Examples

### Fetching Active Articles
```bash
python3 get_active_articles.py
```

### Exporting Tickets to Excel
```bash
python3 ticktets_to_excel_file.py
```

### Fetching Tickets via Shell
```bash
./curl_tickets.sh
```

## Help Center Customizations

## Historical Context

- **Time Period**: 2021-2023
- **Use Case**: Support Engineering workflow automation
- **Status**: Archived (company acquired, Help Center deprecated)
- **Zendesk Version**: Scripts compatible with Zendesk API v2

## Notes & Limitations

- These scripts were designed for a specific Zendesk instance and may require modification for other environments
- API rate limits should be considered when running bulk operations
- Some customizations may not be compatible with newer Zendesk Guide themes
- No longer actively maintained

## Security Reminder

⚠️ **Never commit API credentials to version control.** Use environment variables or secure credential management systems.

## License

These scripts are provided as-is for reference purposes.

---

*Created during tenure as Support Engineer | Last updated: March 2023*
