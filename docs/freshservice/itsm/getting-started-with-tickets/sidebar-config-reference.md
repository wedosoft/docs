# Sidebar Configuration for ITSM Getting Started with Tickets

This file documents the required sidebar.ts configuration for when documents are added to the getting-started-with-tickets folder.

## Required Addition to sidebars.ts

When documents are added, add this section to the main ITSM category:

```typescript
{
  type: 'category',
  label: '🎟️ 티켓 시작하기',
  collapsed: true,
  items: [
    // Add actual document IDs here when documents are created
    // Example:
    // 'freshservice/itsm/getting-started-with-tickets/ticket-creation-basics',
    // 'freshservice/itsm/getting-started-with-tickets/ticket-priority-management',
    // 'freshservice/itsm/getting-started-with-tickets/ticket-workflow-setup',
  ],
},
```

## Integration Point

This should be added to the main Freshservice ITSM section, likely after the existing categories but before the FAQ section.

## Document ID Pattern

When actual documents are added, they should follow this pattern:
- `freshservice/itsm/getting-started-with-tickets/[document-slug]`

## Example Complete Structure

```typescript
{
  type: 'category',
  label: '🔧 Freshservice (ITSM)',
  collapsed: false,
  items: [
    // ... existing categories ...
    {
      type: 'category',
      label: '🎟️ 티켓 시작하기',
      collapsed: true,
      items: [
        'freshservice/itsm/getting-started-with-tickets/ticket-creation-basics',
        'freshservice/itsm/getting-started-with-tickets/ticket-priority-management',
        'freshservice/itsm/getting-started-with-tickets/ticket-workflow-setup',
        'freshservice/itsm/getting-started-with-tickets/ticket-automation-setup',
        'freshservice/itsm/getting-started-with-tickets/ticket-reporting-analytics',
      ],
    },
    // ... rest of ITSM categories ...
  ],
},
```

This configuration will be applied when actual documents are added to the folder.