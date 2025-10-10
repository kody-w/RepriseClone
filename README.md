# Reprise Clone
[Github Pages Link](https://kody-w.github.io/RepriseClone/)


A browser-based demo recording and playback tool, similar to Reprise. Record user interactions on any webpage and replay them later.

## 📚 [View Complete Tutorial](tutorial.html)

New to Reprise Clone? Check out the **[comprehensive tutorial](tutorial.html)** with step-by-step guides for all features!

## Features

- **Recording:**
  - Record full browser sessions with all interactions
  - Capture clicks, form inputs, scrolling, and DOM changes
  - Works on ANY website via bookmarklet (no iframe limitations)
  - Real-time event counter

- **Playback:**
  - Replay recordings with full playback controls
  - **Playback Flags**: Add markers/waypoints to recordings
  - **Step-by-step navigation**: Jump between flags instead of real-time playback
  - **Visual Text Editor**: Browse HTML tree, edit text with live preview
  - **Element Picker**: Click elements on page to select them in tree
  - **Hide/Show Elements**: Remove unwanted overlays, banners, or UI elements
  - **HTML Editor**: Advanced editing with full HTML access
  - **Template Mode**: Mark dynamic vs static elements, export templates
  - **Static Page Animator**: Edit only dynamic elements in static templates
  - Export modified recordings with flags

- Built with [rrweb](https://www.rrweb.io/) - an open-source web session replay library

## Getting Started

### Option 1: Bookmarklet (Recommended - Works on ANY Site!)

The easiest way to record any webpage:

1. Start a local server:
```bash
python -m http.server 8000
```

2. Open http://localhost:8000 in your browser
3. Click "Get Bookmarklet"
4. Drag the "📹 Record Page" button to your bookmarks bar
5. Navigate to ANY webpage you want to record (Google, Microsoft 365, your own sites, etc.)
6. Click the bookmarklet in your bookmarks bar
7. A floating control panel appears - click "Start Recording"
8. Interact with the page normally
9. Click "Stop Recording" then "Export Recording"
10. Load the JSON file in the Player to watch the replay!

**Benefits:**
- Works on external sites (no iframe limitations)
- No CORS issues
- Draggable control panel
- Real-time event counter
- Works on any modern browser

### Option 2: Iframe Recorder (Local Pages Only)

For recording local pages in an embedded iframe:

1. Open `recorder.html`
2. Enter a local URL (like `demo.html`)
3. Click "Load" and then "Start Recording"
4. Interact with the page
5. Click "Stop Recording" and "Export Recording"

**Note:** This method only works for same-origin pages due to browser security restrictions.

## How It Works

### Recording

The recorder uses rrweb to:
1. Take a snapshot of the initial DOM state
2. Monitor all DOM mutations using MutationObserver
3. Capture user interactions (clicks, inputs, scrolling)
4. Record all events with timestamps
5. Export as a JSON file containing the event stream

### Playback

The player uses rrweb-player to:
1. Load the JSON recording file
2. Reconstruct the initial DOM state
3. Replay all events at their original timestamps
4. Provide playback controls (play, pause, speed adjustment)

### Using Playback Flags

Flags allow you to mark important moments and navigate through your recording step-by-step:

1. **Load a recording** in the player
2. Click **"🚩 Flags"** button to open the flags panel
3. **Pause or play** to the moment you want to mark
4. Click **"+ Add Flag at Current Time"**
5. Enter a label (e.g., "Introduction", "Feature Demo", "Conclusion")
6. Optionally add a description
7. Click **"Save Flag"**

**Navigation:**
- Click **"← Prev"** or **"Next →"** to jump between flags
- Click any flag in the list to jump to that moment
- Use keyboard shortcuts: `[` or `←` for previous, `]` or `→` for next
- Click the delete (×) button to remove a flag

**Export:**
- Click **"Export with Flags"** to save the recording with all your flags included
- Flags will be loaded automatically when you import the recording again

**Use Cases:**
- Create step-by-step product demos
- Mark key moments for presentation
- Build interactive tutorials
- Navigate long recordings efficiently

### Editing Text with Visual Tree (Easy Mode)

The powerful visual editor with live preview:

1. Load a recording in the player
2. Click **"✏️ Edit Text"** button
3. A panel slides up from the bottom with:
   - **Left**: HTML tree structure with indentation
   - **Right**: Live text editor
4. **Optional: Click "🗗 Pop Out"** to open the editor in a separate window for full screen space!
5. **Browse the tree** and click any element
6. The element **highlights with purple pulsing outline** on the page
7. **Type in the editor** - changes appear **live on the page**
8. Click **"👁️ Hide Element"** to remove unwanted elements (like recording overlays)
9. Click **"👁️ Show Element"** to restore hidden elements
10. Click **"Exit Text Edit"** when done

**Pop-Out Editor Window:**
- Click **"🗗 Pop Out"** to open the text editor in a separate window
- Gives you full screen space for the recording
- All features work in the popup: tree navigation, live editing, picker mode, hide/show
- Changes sync automatically between windows
- Element highlighting still shows in the main window
- Perfect for dual monitor setups!

**Features:**
- Visual HTML tree structure with indentation
- Elements with text highlighted in blue
- Live preview - changes as you type
- Purple pulsing outline shows selected element
- Auto-scroll to selected element
- 🎯 **Element Picker** - click on the page to select elements (shows in tree!)
- 🔍 **Find Text** - search for specific text
- 👁️ **Hide/Show Elements** - remove unwanted overlays, banners, etc.
- **Show All Hidden** - restore all hidden elements at once
- Hidden elements shown with strikethrough in tree

**Element Picker Mode:**
1. Click **"🎯 Pick Element from Page"**
2. Cursor changes to crosshair
3. Hover over elements - **ALL stacked elements highlight with different colors** (pyramid effect like Chrome DevTools!)
4. Tooltip shows all elements in the stack with color indicators
5. Click to select the **deepest** element at that position
6. Click the **same spot again** to cycle up through the element stack
7. Shows "(X of Y)" to track position in stack
8. Selected element automatically highlights in the HTML tree with **bright purple pulsing glow**
9. Element is ready to edit!

**Perfect for:**
- Editing text without code knowledge
- Removing recording overlays and banners
- Cleaning up demos
- Updating product names or values
- Hiding unwanted UI elements

**Note:** Hidden elements persist across playback! When you hide an element, it will stay hidden even when you scrub through the recording timeline. This ensures your edits remain visible throughout the entire playback.

### Exporting Edited Recordings

After making changes to your recording (editing text, hiding elements, etc.), you can export a new version:

1. Make your edits using the text editor
2. Hide any unwanted elements
3. Click **"💾 Export Edited Recording"** at the bottom of the text editor panel
4. The exported file will contain:
   - All original recording events
   - Your edited HTML with all changes
   - All flags you've added
   - An "EDITED" indicator

**Loading Edited Recordings:**
- When you load an edited recording, it will automatically display your changes
- The recording info will show an **✏️ EDITED** badge
- All text edits and hidden elements are preserved
- You can continue editing and export again

**Use Cases:**
- Clean up recordings by removing overlays before sharing
- Update product names or pricing in demos
- Hide sensitive information before exporting
- Create polished presentations from raw recordings

### Editing HTML (Advanced Mode)

For advanced users who want full control:

1. Load a recording and pause at the desired moment
2. Click **"Edit HTML"** button
3. The HTML editor panel opens on the right
4. Edit the HTML directly in the editor
5. Click **"Apply Changes"** to update the replay
6. Use **"Refresh HTML"** to reload current HTML
7. Use **"Copy HTML"** to copy to clipboard
8. Press **ESC** to close the editor

**Use Cases:**
- Complex layout changes
- Modifying styles, images, or attributes
- Advanced customization
- Developers who prefer code editing

### Template Mode (Separate Static from Dynamic Content)

Template Mode lets you mark which elements are dynamic (like chat messages) versus static (like headers, navigation):

1. Load a recording in the player
2. Click **"🎬 Template Mode"** button
3. Open the **"✏️ Edit Text"** panel
4. Browse the HTML tree and select dynamic elements
5. Click **"🎬 Mark as Dynamic"** for each dynamic element
   - Dynamic elements get a blue background and 🎬 badge
6. Click **"📤 Export Template + Mapping"**
   - Downloads **template HTML** (static content only, dynamic elements removed)
   - Downloads **mapping JSON** (list of dynamic element selectors)
7. Click **"📥 Load Template"** to reverse the process:
   - Upload a template HTML
   - System auto-detects what's dynamic vs static
   - Marks detected elements for animation

**What gets exported:**
- `template-{timestamp}.html` - Static HTML page with dynamic elements removed
- `template-mapping-{timestamp}.json` - JSON file mapping dynamic element selectors

**Use Cases:**
- Create reusable templates for product demos
- Separate UI chrome from dynamic content
- Define which parts animate during playback
- Build template libraries for consistent demos

### Static Page Animator (Edit Dynamic Elements Only)

The Static Page Animator is a specialized tool for editing ONLY the dynamic elements in a static template:

1. Click **"🎨 Open Static Page Animator"** from Template Mode panel
   - Or navigate to `animator.html` directly
2. Upload the **template HTML** file
3. Upload the **mapping JSON** file
4. The page loads with dynamic elements highlighted
5. Click any dynamic element to edit its content
6. Static elements are locked 🔒 and show "cannot be edited" message
7. Make changes in the live editor
8. Click **"✓ Apply"** to save changes
9. Click **"↶ Revert"** to restore original content

**Features:**
- **Live preview** - See changes as you type
- **Click to select** - Click elements on the page or in the list
- **Locked static elements** - Can't accidentally edit template structure
- **Visual indicators** - Dynamic elements pulse with purple outline
- **Original content** - Always able to revert to original

**Perfect for:**
- Updating chat messages in demos
- Changing dynamic data without touching template
- Creating variations of the same template
- Non-technical users editing specific content areas
- Protecting template structure while allowing content updates

**Workflow Example:**
```
1. Record a chat conversation
2. Mark chat messages as dynamic (🎬)
3. Export template + mapping
4. Open Static Page Animator
5. Load template + mapping
6. Edit chat messages only
7. Static header/sidebar are locked
8. Export edited version
```

## Recording Tips

1. **Use the Bookmarklet**: The bookmarklet works on ANY webpage, including external sites
2. **Test with Demo Page**: Use the included `demo.html` for testing all features
3. **File size**: Complex pages with many interactions can produce large JSON files
4. **Draggable Controls**: The bookmarklet control panel can be dragged anywhere on the page
5. **Multiple Recordings**: Each export gets a unique timestamp - you can record multiple sessions

## File Structure

```
RepriseClone/
├── index.html          # Main landing page
├── tutorial.html       # Complete step-by-step tutorial (START HERE!)
├── bookmarklet.html    # Bookmarklet installation page (RECOMMENDED)
├── recorder.html       # Iframe-based recording interface
├── player.html         # Playback interface with editing tools
├── animator.html       # Static Page Animator for template editing
├── demo.html          # Sample page for testing
├── styles.css         # Shared styles
└── README.md          # This file
```

## Technologies Used

- [rrweb](https://www.rrweb.io/) - Session recording and replay
- [rrweb-player](https://github.com/rrweb-io/rrweb-player) - Playback UI with controls
- Vanilla JavaScript - No build tools required
- HTML5/CSS3 - Modern web standards

## Limitations

- Some dynamic content (WebGL, Canvas) may not replay perfectly
- Video and audio playback timing may differ
- Third-party iframes within the recorded page won't be captured
- Very large pages with thousands of events can produce large files

## Future Enhancements

- Cloud storage for recordings
- Annotation tools for highlighting during playback
- Recording editing capabilities (trim, cut, merge)
- Multiple session comparison
- Custom branding and watermarks
- Screenshot capture at key moments

## License

This is a demo project for educational purposes. rrweb is licensed under MIT.

## Credits

Built with [rrweb](https://www.rrweb.io/) by the rrweb team.
