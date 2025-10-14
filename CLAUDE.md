# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Reprise Clone** is a browser-based demo recording and playback tool with a revolutionary meta-layer visualization system. It combines:
1. **Recording/Playback Tools** - Built on rrweb for capturing and replaying web interactions
2. **Meta-Layer System** - A 15-layer nested reality visualization from the Big Bang to individual pixels
3. **Historical Replicas** - Period-accurate recreations of computing applications (AIM, MySpace, Facebook, Discord, etc.)

Live demo: https://kody-w.github.io/RepriseClone/

## Development Setup

This project requires **no build step** - it's pure HTML/CSS/JavaScript.

### Running Locally

```bash
# Option 1: Python (recommended)
python -m http.server 8000

# Option 2: Node.js
npx http-server -p 8000

# Option 3: PHP
php -S localhost:8000
```

Then open http://localhost:8000

### Testing

No automated test suite exists. Manual testing workflow:
1. Test recording with the bookmarklet on various sites
2. Test playback in player.html with exported recordings
3. Test meta-layer transitions in universal-consciousness.html
4. Test iframe communication between nested layers

## Architecture

### Core Recording System

**Technology Stack:**
- **rrweb** (https://www.rrweb.io/) - Session recording/replay engine
- **rrweb-player** - Playback UI with controls
- Vanilla JavaScript (ES6+) - No frameworks or build tools

**Recording Flow:**
1. Bookmarklet injects rrweb library into target page
2. rrweb.record() captures DOM snapshots + mutations + events
3. Events stored in `window.repriseRecorder.events` array
4. Export creates JSON with format: `{version, timestamp, url, events: []}`
5. Player loads JSON and uses rrweb.Replayer for playback

**Key Files:**
- `bookmarklet.html` - Generates draggable bookmarklet recorder (RECOMMENDED method)
- `recorder.html` - Iframe-based recorder (same-origin only, legacy)
- `player.html` - Full-featured playback with editing panels

### Meta-Layer System

A unique visualization concept showing computing in cosmic context through 15 nested layers.

**Layer Hierarchy:**
```
∞ (The Void)
└─ 4D Hypercube (Spacetime visualization)
   └─ Multiverse (Branching timelines)
      └─ Observable Universe (13.8 billion years)
         └─ Milky Way Galaxy
            └─ Solar System
               └─ Earth
                  └─ 2050 Neural Memory Interface
                     └─ Memory Browser (Lifetime of computing)
                        └─ Spatial Zoom (Earth → City → Building → Room)
                           └─ Physical Room Environment (1999-2024 era rooms)
                              └─ Computer Hardware (CRT, iMac, Gaming PC)
                                 └─ Boot Sequence (BIOS, POST, OS)
                                    └─ Operating System Desktop
                                       └─ Browser Window
                                          └─ Web Application (AIM, Discord, etc.)
```

**Key Meta-Layer Files:**
- `universal-consciousness.html` - Entry point, cosmic zoom from Big Bang
- `memory-dive.html` - 2050 neural interface, memory browser
- `immersive-environment.html` - Period-accurate physical rooms (1999-2024)
- `boot-simulation.html` - Complete boot sequence with authentic audio
- `meta-evolution.html` - Hardware evolution viewer (CRT → Gaming PC)
- `4d-timeline.html` - Branching timeline multiverse navigation
- `visual-history.html` - Flipbook-style version navigation

**Iframe Communication Pattern:**
```javascript
// Parent loads child in iframe
document.getElementById('childFrame').src = 'child-layer.html';

// Child can communicate up via postMessage if needed
window.parent.postMessage({type: 'layerLoaded'}, '*');
```

Maximum iframe nesting depth is 3 levels for performance.

### Audio System

All sounds synthesized using Web Audio API (no audio files):

```javascript
// Example: BIOS beep
function playBIOSBeep() {
    const context = new AudioContext();
    const oscillator = context.createOscillator();
    const gainNode = context.createGain();

    oscillator.connect(gainNode);
    gainNode.connect(context.destination);

    oscillator.frequency.value = 800; // Hz
    oscillator.type = 'sine';

    gainNode.gain.setValueAtTime(0.3, context.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(0.01, context.currentTime + 0.2);

    oscillator.start();
    oscillator.stop(context.currentTime + 0.2);
}
```

**Sound Frequencies:**
- BIOS beep: 800 Hz sine
- Mac startup: C5-E5-G5 chord (523.25, 659.25, 783.99 Hz)
- Windows melody: C5→E5→G5→C6 ascending
- Cosmic tones: 50-800 Hz range
- Neural hums: 120 Hz ambient

**IMPORTANT:** Audio requires user interaction to start (browser security). Always call audio functions in response to clicks/keypresses.

### Editing Tools

**Player Features (`player.html`):**
- **Playback Flags** - Add markers at key moments, jump between them with `[` `]` keys
- **Visual Text Editor** - Browse HTML tree, edit text, hide elements
- **Element Picker** - Click elements on replayed page to select them
- **HTML Editor** - Direct HTML editing for advanced changes
- **Template Mode** - Mark dynamic vs static elements, export reusable templates
- **Frame Export** - Export individual frames (50-90% smaller than full recordings)

**Standalone Editors:**
- `animator.html` - Two modes: template editing (edit dynamic elements only) + frame animation (play through frame sequence)
- `wysiwyg-editor.html` - Visual editor with rich text toolbar, no code knowledge needed
- `frame-splitter.html` - Extract HTML → separate HTML/CSS/JS files for modular projects
- `multiframe-editor.html` - Batch edit multiple frames, opens in new window

### Historical Demo Applications

Located in `demos/` directory. Each is a standalone HTML file recreating historical UIs:

- `aim-1999.html` - AOL Instant Messenger with buddy list
- `msn-2001.html` - MSN Messenger with butterfly logo
- `myspace-2005.html` - MySpace profile customization
- `facebook-2007.html` - Facebook with "The Wall" and Poke
- `twitter-2009.html` - Twitter with 140 character limit
- `instagram-2012.html` - Instagram photo-first design
- `discord-2024.html` - Modern Discord with dark theme

These demos are loaded in various meta-layers and can be used in the visual history player.

## Common Development Tasks

### Adding a New Demo Application

1. Create new HTML file in `demos/` (e.g., `demos/slack-2015.html`)
2. Use inline styles to recreate period-accurate UI
3. Add to demo arrays in `visual-history.html`:
```javascript
const messagingDemos = [
    'demos/aim-1999.html',
    'demos/msn-2001.html',
    'demos/slack-2015.html', // New demo
    'demos/discord-2024.html'
];
```
4. Update memory timeline in `memory-dive.html` if creating a memory:
```javascript
const memories = [
    {year: 1999, title: 'First Online Conversation', app: 'AIM', ...},
    {year: 2015, title: 'New Memory Title', app: 'Slack', ...}, // New
];
```

### Adding a New Meta-Layer

1. Create new HTML file (e.g., `quantum-layer.html`)
2. Follow the cosmic layer CSS pattern:
```css
.cosmic-layer {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    opacity: 0;
    transform: scale(0);
    transition: all 3s ease-in-out;
}
.cosmic-layer.active {
    opacity: 1;
    transform: scale(1);
}
```
3. Add navigation button in parent layer
4. Add iframe loading or direct transition logic
5. Update layer depth counter in info display

### Modifying Boot Sequence

Edit `boot-simulation.html`:
- **Hardware Shells** - Modify CSS for `.hardware-shell` classes (CRT, iMac, Gaming PC styles)
- **Boot States** - Sequential flow: OFF → POST → BOOTING → DESKTOP → BROWSER → APP
- **OS Customization** - Each era has its own `.desktop-{era}` class
- **Audio** - Update frequency values in `playBIOSBeep()`, `playMacStartupChime()`, `playWindowsStartup()`

### Creating Bookmarklet Variations

Edit `bookmarklet.html` script section:
```javascript
const bookmarkletCode = `
(function() {
    // Your custom recorder logic here
    // Must be minified and URI-encoded
})();
`;
document.getElementById('bookmarklet').href = 'javascript:' + encodeURIComponent(bookmarkletCode.trim());
```

Test by dragging to bookmarks bar and using on external sites.

## File Organization

```
/
├── index.html                    # Main hub with navigation cards
├── styles.css                    # Shared global styles
│
├── META-LAYER SYSTEM
├── universal-consciousness.html  # 15-layer entry point
├── memory-dive.html              # 2050 neural memory interface
├── immersive-environment.html    # Physical room environments
├── boot-simulation.html          # Complete boot with audio
├── visual-history.html           # Flipbook player with demo buttons
├── meta-evolution.html           # Hardware evolution (CRT → Gaming PC)
├── 4d-timeline.html             # Branching timeline multiverse
│
├── RECORDING & PLAYBACK
├── bookmarklet.html             # Bookmarklet installer (RECOMMENDED)
├── recorder.html                # Iframe recorder (local only, legacy)
├── player.html                  # Playback with editing panels
├── animator.html                # Template editing + frame animation
├── wysiwyg-editor.html          # WYSIWYG visual editor
├── frame-splitter.html          # HTML → modular files
├── multiframe-editor.html       # Batch frame editor
│
├── DEMOS (Historical App Replicas)
├── demos/aim-1999.html
├── demos/msn-2001.html
├── demos/myspace-2005.html
├── demos/facebook-2007.html
├── demos/twitter-2009.html
├── demos/instagram-2012.html
├── demos/discord-2024.html
│
├── DOCUMENTATION
├── tutorial.html                # Step-by-step tutorial
├── docs.html                    # Complete documentation
├── quick-reference.html         # Quick reference guide
└── demo.html                    # Test page for recording
```

## Key Concepts

### rrweb Event Structure

```javascript
{
    version: '1.0',
    timestamp: '2024-10-14T12:00:00.000Z',
    url: 'https://example.com',
    events: [
        {type: 4, data: {...}},  // Full snapshot
        {type: 3, data: {...}},  // DOM mutation
        {type: 2, data: {...}},  // Mouse event
        // ... more events
    ]
}
```

Event types: 0=DomContentLoaded, 1=Load, 2=FullSnapshot, 3=IncrementalSnapshot, 4=Meta, 5=Custom

### Template Mode Workflow

1. Record or load demo in player.html
2. Enable Template Mode in player
3. Click elements to mark as dynamic (editable) or static (locked)
4. Export template + mapping JSON
5. Load in animator.html with mapping
6. Edit only dynamic content
7. Export frames
8. Polish in wysiwyg-editor.html if needed

### Era-Specific Styling

When creating period-accurate content:
- **1999**: Beige (#f5f5dc), CRT effects, Comic Sans, bright colors
- **2001**: Translucent blues/greens, rounded corners, iMac aesthetic
- **2005**: Web 2.0 gradients, badges, Tahoma font, bright orange/blue
- **2007**: Minimal grays, Helvetica, clean rectangles, subtle shadows
- **2024**: Dark themes, RGB accents, high contrast, glassmorphism

## Browser Compatibility

- **Recommended**: Chrome/Edge (best performance for 3D transforms)
- **Supported**: Firefox, Safari
- **Known Issues**:
  - Safari requires page click before audio plays
  - Firefox 3D transforms less smooth than Chrome
  - Mobile view of meta-layers not optimized

## Performance Considerations

- Full rrweb recordings: 10-50 MB for complex pages
- Frame animations: 50-90% smaller (no event stream)
- Deep iframe nesting (3+ levels) impacts performance
- Canvas/3D transforms require GPU acceleration
- Large recordings may slow on older devices

## Git Workflow

Current branch: `main`

When committing changes, focus commit messages on "why" not "what". The project uses descriptive commits that explain the purpose of changes.

Example: "Enhance Frame Editor: Add view mode toggle for visual and tree views, implement element duplication functionality, and improve UI interactions"

## Limitations & Known Issues

**Recording:**
- WebGL/Canvas content may not replay perfectly
- Video/audio timing may differ in replay
- Third-party iframes not captured
- Very large pages = large file sizes

**Meta-Layers:**
- Audio requires user interaction (browser security)
- Deep iframe nesting may impact performance
- 3D transforms require modern browser
- Some effects disabled on mobile

## Philosophy

This project explores **scale, context, and meaning** in computing. Every interaction exists within nested layers of reality - from atoms to cosmos. The meta-layer system makes these abstractions visible and experiential.

Computing doesn't happen in isolation - it happens in rooms, in moments, in lives, in history, in the universe.
