## 2024-05-24 - Added aria-labels to Session Action Buttons
**Learning:** Icon-only buttons used for critical session management functions (create, rename, delete) were missing `aria-label` attributes, making them inaccessible to screen readers. This is a common pattern in the app.
**Action:** Always verify that buttons containing only SVGs (like those in `Sessions` component) have an `aria-label` attribute describing their action.
