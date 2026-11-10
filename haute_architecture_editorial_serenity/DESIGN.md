---
name: Haute Architecture & Editorial Serenity
colors:
  surface: '#fcf9f3'
  surface-dim: '#dcdad4'
  surface-bright: '#fcf9f3'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3ed'
  surface-container: '#f0eee8'
  surface-container-high: '#ebe8e2'
  surface-container-highest: '#e5e2dc'
  on-surface: '#1c1c18'
  on-surface-variant: '#4e453c'
  inverse-surface: '#31312d'
  inverse-on-surface: '#f3f0ea'
  outline: '#80756a'
  outline-variant: '#d1c4b8'
  surface-tint: '#745a37'
  primary: '#745a37'
  on-primary: '#ffffff'
  primary-container: '#b99a72'
  on-primary-container: '#473213'
  inverse-primary: '#e3c196'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e4e2e1'
  on-secondary-container: '#656464'
  tertiary: '#645e53'
  on-tertiary: '#ffffff'
  tertiary-container: '#a69e91'
  on-tertiary-container: '#3b352c'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffddb3'
  primary-fixed-dim: '#e3c196'
  on-primary-fixed: '#291800'
  on-primary-fixed-variant: '#5a4322'
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#ebe1d3'
  tertiary-fixed-dim: '#cfc5b8'
  on-tertiary-fixed: '#1f1b13'
  on-tertiary-fixed-variant: '#4c463c'
  background: '#fcf9f3'
  on-background: '#1c1c18'
  surface-variant: '#e5e2dc'
typography:
  display:
    fontFamily: Playfair Display
    fontSize: 4rem
    fontWeight: '400'
    lineHeight: 4.5rem
    letterSpacing: -0.02em
  display-mobile:
    fontFamily: Playfair Display
    fontSize: 2.5rem
    fontWeight: '400'
    lineHeight: 3rem
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 2.75rem
    fontWeight: '400'
    lineHeight: 3.25rem
    letterSpacing: -0.015em
  headline-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 2rem
    fontWeight: '400'
    lineHeight: 2.5rem
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Playfair Display
    fontSize: 2rem
    fontWeight: '400'
    lineHeight: 2.5rem
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Playfair Display
    fontSize: 1.375rem
    fontWeight: '500'
    lineHeight: 1.875rem
    letterSpacing: 0em
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 1.125rem
    fontWeight: '300'
    lineHeight: 1.875rem
    letterSpacing: 0.01em
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: 1.625rem
    letterSpacing: 0.005em
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.875rem
    fontWeight: '400'
    lineHeight: 1.375rem
    letterSpacing: 0.01em
  label-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.875rem
    fontWeight: '600'
    lineHeight: 1.25rem
    letterSpacing: 0.08em
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.75rem
    fontWeight: '500'
    lineHeight: 1rem
    letterSpacing: 0.12em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.6875rem
    fontWeight: '600'
    lineHeight: 0.875rem
    letterSpacing: 0.15em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-mobile: 1rem
  margin: 4rem
  margin-mobile: 1.25rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 2rem
  space-xl: 3.5rem
---

## Brand & Style
This design system defines an ultra-luxury digital experience tailored to discerning global clientele, high-net-worth investors, and architectural connoisseurs. The brand evokes stillness, discretion, and curation—reminiscent of private salon exhibitions and prestige architectural monographs.

The visual direction balances haute-couture editorial layouts with modern Swiss grid discipline. Interactions are deliberate, weighted, and unhurried. Generous negative space frames architectural imagery like physical gallery walls, while meticulous hairline accents provide structural definition without decorative noise. The interface avoids aggressive conversion hooks, opting instead for bespoke confidence, tactile restraint, and architectural permanence.

## Colors
The palette is rooted in natural limestone, raw silk, and patinated architectural metals:
- **Primary (`#B99A72` - Champagne Gold):** Used sparingly for intentional focal points: active states, key interactive indicators, and bespoke property badges. It must never coat mass backgrounds.
- **Secondary (`#252525` - Deep Onyx / Charcoal):** The anchor for high-legibility typography, primary CTA fills, and crisp framing elements. Replaces harsh pure black with a warmer, oil-based charcoal tone.
- **Tertiary (`#E9DFD1` - Soft Beige):** Applied to structural hairline borders, quiet container divisions, and alternating editorial surface modules.
- **Neutral (`#F8F5EF` - Warm Ivory):** The foundational canvas color. Replaces standard stark white to eliminate digital glare and impart the tactile quality of heavy cotton rag paper.
- **Crisp White (`#FFFFFF`):** Reserved strictly for image backplates, high-contrast modal trays, and elevated card canvases.

## Typography
The typographic hierarchy creates a dialogue between classical architectural gravitas and functional modern precision.

- **Playfair Display** serves as the voice of prestige across hero banners, estate naming, and editorial pull-quotes. Display and headline levels preserve natural italic variants for emphasis, estate classifications, or location coordinates.
- **Plus Jakarta Sans** provides clarity across data specifications, architectural floorplan measures, pricing, and narrative body text. Its subtle geometric warmth prevents cold clinical reading.
- **Metadata and labels (`label-lg`, `label-md`, `label-sm`)** are strictly styled in uppercase with tracking between `0.08em` and `0.15em` to reinforce an editorial, monograph-style cadence. Numerical currency and metric dimensions use standard tabular numerals (`tnum`).

## Layout & Spacing
The layout adheres to a fixed-max-width 12-column system (max-width `1440px`), expanding outward with broad canvas breathing room on ultra-wide screens. 

- **Desktop (1024px+):** 12 columns with `1.5rem` gutters and generous `4rem` outer canvas padding. Sections incorporate alternating asymmetry (e.g., 7-column hero photographs paired with 5-column offset descriptions).
- **Tablet (768px - 1023px):** 8 columns with `1.25rem` gutters and `2.5rem` outer margins. Multi-column property metrics condense to 2-column configurations.
- **Mobile (<768px):** 4 columns with `1rem` gutters and `1.25rem` canvas margins. Hero imagery breaks bleed to the edge, while textual narratives maintain internal margins.

Vertical rhythm relies on intentional decompression. Section spacing alternates between `space-lg` for tightly coupled data clusters and `space-xl` (expanding dynamically up to `6rem` on desktop displays) between editorial chapters.

## Elevation & Depth
Depth is articulated primarily through layered materiality and delicate ambient shadows rather than stark mechanical drops.

- **Tonal Hierarchy:** The primary base is Warm Ivory (`#F8F5EF`). Interactive cards and active detail sheets transition up to Crisp White (`#FFFFFF`).
- **Hairline Boundaries:** Surface transitions rely on crisp 1px borders in Soft Beige (`#E9DFD1`), providing structural order without visual weight.
- **Ambient Diffusion:** Shadows emulate natural, filtered gallery daylight. They feature a multi-layer spread using Deep Onyx tinted at 4–7% opacity with wide blur radiuses (`0 12px 32px -4px rgba(37, 37, 37, 0.05)`).
- **Glass Transparency:** Floating navigation bars and image badges employ subtle translucency (`rgba(248, 245, 239, 0.85)`) coupled with a heavy backdrop blur (`16px`), letting photography hint through structural Chrome.

## Shapes
In harmony with bespoke architecture, corners remain taut, disciplined, and refined. 

- UI elements employ **Soft Roundedness (Level 1)**: default components carry a precise `0.25rem` (4px) radius, lending an architectural edge that is crisp without feeling hostile.
- Containers and expansive property gallery cards scale to `0.5rem` (8px). 
- Fully round pill geometries (`rounded-full`) are reserved exclusively for compact micro-pills, such as status markers, private inquiry badges, and floorplan toggles.

## Components

### Buttons & Interactive Triggers
- **Primary:** Deep Onyx (`#252525`) solid fill with Crisp White text. Clean 4px corner radius, standard vertical padding of `0.875rem`, horizontal padding of `1.75rem`. Text set in `label-md` with `0.1em` letter-spacing. Subtle hover transition to a Champagne Gold border accent.
- **Secondary / Ghost:** Transparent background enclosed in a 1px Soft Beige (`#E9DFD1`) border, with Deep Onyx text. On hover, the background softly shifts to Soft Beige at 40% opacity.
- **Text Link:** Deep Onyx text accompanied by a permanent ultra-fine 1px Champagne Gold underline positioned `4px` below the baseline. Hover smoothly transitions the underline to Charcoal.

### Property Display Cards
- Composed of an edge-to-edge `4:5` or `16:10` architectural photography viewport, set inside a Crisp White frame with a 1px Soft Beige border.
- **Overlays:** A Champagne Gold hairline badge displays listing status ("Private Collection", "Available") anchored in the upper-left corner with ivory frosted-glass backing.
- **Metadata Tray:** Nested below the image, featuring title in Playfair Display (`headline-sm`), followed by architectural metrics (Square Footage, Suites, Region) rendered in `label-sm` with fine vertical divider pipes (`|`).

### Form Elements & Inquiries
- **Input Fields:** Unfilled backgrounds resting on a 1px Soft Beige bottom border (or complete rectangular enclosure for inputs). Focus state transitions the border to Champagne Gold (`#B99A72`) without outer focus rings. Labels sit as uppercase micro-caps (`label-sm`).
- **Checkboxes & Radios:** Scaled down to an unobtrusive 16px footprint. Charcoal fill on selection with white architectural checks. Unselected state bordered in Soft Beige.

### Filter Chips & Navigation Badges
- Low-profile pill or 4px soft rectangles. Default state uses transparent fill with Soft Beige border. Selected state swaps to Deep Onyx fill with Crisp White typography, avoiding loud primary saturation.

### Architectural Inspection Panes (Drawers / Modals)
- Full-height side drawers sliding in from the right edge with a Warm Ivory canvas. Hairline dividers, extensive white space around floor plans, high-res spec tables, and a sticky "Schedule Private Viewing" action bar.