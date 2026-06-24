# Messenger Bridge Setup

## Supported platforms

| Platform | Adapter | Required config |
|----------|---------|-----------------|
| WhatsApp | whatsapp-auto-responder | Bridge daemon or Web API session |
| Telegram | Bot API | `TELEGRAM_BOT_TOKEN`, chat ID |
| Future | Extensible adapter interface | Per-platform credentials |

## Unified message schema

```json
{
  "platform": "whatsapp|telegram",
  "sender_id": "string",
  "contact_name": "string",
  "body": "string",
  "timestamp": "ISO8601",
  "attachments": []
}
```

## Policy stack (strictest wins)

1. `privacy-redactor` on all inbound and outbound text
2. `whatsapp-message-rater` (or equivalent) before any reply
3. `hitl-approver` for medium+ risk or financial/legal content
4. Rate limit: 10 auto-replies/hour/contact across all platforms

## Per-contact settings

Store in semantic-memory-manager:

```
contact:<id>:auto_reply = true|false
contact:<id>:priority = normal|high
contact:<id>:platforms = [whatsapp, telegram]
```

## First-run checklist

1. Confirm which platforms are connected
2. Set default auto_reply to **false**
3. Test with one inbound message end-to-end (rate -> draft -> HITL -> send)
4. Enable auto_reply per contact only after successful test