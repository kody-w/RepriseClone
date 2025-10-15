# Conversation JSON Format

## Overview
The Chat Animator supports a structured JSON format for importing and exporting conversations. Each message can have multiple separate fields that are independently editable.

## JSON Structure

```json
{
  "messages": [
    {
      "id": 0,
      "type": "agent",
      "title": "Support Agent",
      "subtitle": "Analyzing your request...",
      "text": "Main message content here",
      "timestamp": "2:30 PM",
      "posX": 50,
      "posY": 100
    }
  ],
  "metadata": {
    "created": "2025-10-15T21:45:00.000Z",
    "totalMessages": 1,
    "version": "1.0"
  }
}
```

## Message Fields

### Required Fields

- **`id`** (number): Unique identifier for the message
- **`type`** (string): Either `"agent"` or `"customer"`
- **`text`** (string): The main message content
- **`posX`** (number): Horizontal position in pixels
- **`posY`** (number): Vertical position in pixels

### Optional Fields

- **`title`** (string):
  - For agent messages: Agent name/role (e.g., "Support Agent", "Planning Agent")
  - For customer messages: Usually left empty
  - Displays as bold text at the top of the message bubble

- **`subtitle`** (string):
  - Secondary text shown below the title
  - Styled in italic with reduced opacity
  - Great for status indicators (e.g., "Typing...", "Analyzing request...")
  - Leave empty or omit if not needed

- **`timestamp`** (string):
  - Time indicator for the message
  - Can be any format (e.g., "2:30 PM", "14:30", "Just now")
  - Displays in small text at bottom-right of message
  - Leave empty or omit if not needed

## Field Visibility in UI

When editing a message in Chat Animator:

1. **Title/Name**: Always visible (shows for both agent and customer, but typically used for agents)
2. **Subtitle**: Toggle checkbox "Show Subtitle" to display input field
3. **Message Text**: Always visible
4. **Timestamp**: Toggle checkbox "Show Timestamp" to display input field
5. **Position X/Y**: Always visible

## Example Use Cases

### Simple Conversation (minimal fields)
```json
{
  "messages": [
    {
      "id": 0,
      "type": "customer",
      "title": "",
      "subtitle": "",
      "text": "Hello!",
      "timestamp": "",
      "posX": 500,
      "posY": 50
    },
    {
      "id": 1,
      "type": "agent",
      "title": "Agent",
      "subtitle": "",
      "text": "Hi! How can I help?",
      "timestamp": "",
      "posX": 50,
      "posY": 150
    }
  ]
}
```

### Rich Conversation (all fields)
```json
{
  "messages": [
    {
      "id": 0,
      "type": "agent",
      "title": "Planning Agent",
      "subtitle": "Analyzing your project structure...",
      "text": "I've reviewed your codebase and found 3 optimization opportunities:\n\n1. Database queries\n2. API caching\n3. Image compression",
      "timestamp": "2:45 PM",
      "posX": 50,
      "posY": 50
    }
  ]
}
```

## Tips

1. **Line Breaks**: Use `\n` in the text field for multi-line messages
2. **Empty Fields**: Optional fields can be empty strings `""` or omitted entirely
3. **Positioning**:
   - Typical agent message X position: `50` (left side)
   - Typical customer message X position: `500` (right side)
   - Vertical spacing: Increment Y by 100-150 pixels per message
4. **Backwards Compatibility**: Old JSON files without `subtitle` and `timestamp` will still work

## Import Methods

1. **File Upload**: Click "📥 Import Conversation" → Upload .json file
2. **Copy/Paste**: Click "📥 Import Conversation" → Paste JSON in textarea

## Export

Click "💬 Export Conversation" to download a complete JSON file with all message fields and metadata.

---

## Template Placeholders (Advanced)

When you import custom message templates from the Chat Frame Generator, you can use these placeholders in your HTML templates. The Chat Animator will automatically replace them with values from your JSON.

### Available Placeholders

| Placeholder | JSON Field | Description | Works For |
|------------|------------|-------------|-----------|
| `{{AGENT_TITLE}}` | `title` | Agent name/role | Agent messages only |
| `{{TITLE}}` | `title` | Generic title | Both agent & customer |
| `{{SUBTITLE}}` | `subtitle` | Secondary text below title | Both agent & customer |
| `{{MESSAGE_TEXT}}` | `text` | Main message content | Both agent & customer |
| `{{TEXT}}` | `text` | Alternative for message text | Both agent & customer |
| `{{TIMESTAMP}}` | `timestamp` | Time indicator | Both agent & customer |

### Example Template with All Placeholders

**Agent Message Template HTML:**
```html
<div class="agent-bubble">
  <div class="agent-header">
    <strong>{{AGENT_TITLE}}</strong>
  </div>
  <div class="agent-subtitle">{{SUBTITLE}}</div>
  <div class="agent-body">{{MESSAGE_TEXT}}</div>
  <div class="agent-time">{{TIMESTAMP}}</div>
</div>
```

**Your JSON:**
```json
{
  "id": 0,
  "type": "agent",
  "title": "Planning Agent",
  "subtitle": "Analyzing your request...",
  "text": "I found 3 optimization opportunities.",
  "timestamp": "2:30 PM",
  "posX": 50,
  "posY": 50
}
```

**Rendered Output:**
```html
<div class="agent-bubble">
  <div class="agent-header">
    <strong>Planning Agent</strong>
  </div>
  <div class="agent-subtitle">Analyzing your request...</div>
  <div class="agent-body">I found 3 optimization opportunities.</div>
  <div class="agent-time">2:30 PM</div>
</div>
```

### Smart Empty Field Handling

The Chat Animator automatically removes empty HTML elements when fields are blank:

```json
{
  "title": "Agent",
  "subtitle": "",      // Empty
  "text": "Hello!",
  "timestamp": ""      // Empty
}
```

Empty `<div>` tags for subtitle and timestamp will be automatically removed from the rendered HTML.

### Tips for Template Design

1. **Always include placeholders** in your templates if you want dynamic content
2. **Use semantic HTML** - wrap placeholders in appropriate elements (div, span, p, etc.)
3. **Style with CSS** - Add classes to your template elements for consistent styling
4. **Test with sample data** - Import the `sample-conversation.json` to see how your templates render
