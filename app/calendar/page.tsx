'use client';

import { useState } from "react";
import { Calendar, CalendarEvent, CalendarProps } from "./components/Calendar";
import { UpcomingEvents } from "./components/UpcomingEvents";

const MOCK_EVENTS: CalendarEvent[] = [
  {
    "id": "event-0",
    "name": "Event #1",
    "startDateTime": "2025-01-14T08:00:00.000Z",
    "endDateTime": "2025-01-14T08:00:00.000Z",
    "rsvpUrl": ""
  },
  {
    "id": "event-1",
    "name": "Event #2",
    "startDateTime": "2025-01-18T08:00:00.000Z",
    "endDateTime": "2025-01-18T08:00:00.000Z",
    "rsvpUrl": ""
  },
  {
    "id": "event-2",
    "name": "Event #3",
    "startDateTime": "2025-01-21T08:00:00.000Z",
    "endDateTime": "2025-01-21T08:00:00.000Z",
    "rsvpUrl": ""
  },
  {
    "id": "event-3",
    "name": "Event #4",
    "startDateTime": "2025-01-30T08:00:00.000Z",
    "endDateTime": "2025-01-30T08:00:00.000Z",
    "rsvpUrl": ""
  }
]

export default function MemberPage() {
  const [selected, setSelected] = useState<Date | undefined>();

  const handleOnDayClick: CalendarProps['onDayClick'] = (day, modifiers) => {
    setSelected(day)
  }

  return <div className="flex items-center justify-center h-full">
    <div className="flex items-center gap-x-4">
      <Calendar
        events={MOCK_EVENTS}
        onDayClick={handleOnDayClick}
      />
      <UpcomingEvents events={MOCK_EVENTS}/>
    </div>
    
  </div>;
}
