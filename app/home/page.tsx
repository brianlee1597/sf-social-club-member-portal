"use client";
import { useAppSelector } from "@/lib/hooks";
import { Calendar, CalendarEvent } from "../calendar/components/Calendar";
import { WelcomeMessage } from "./WelcomeMessage";

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

export default function HomePage() {
  return (
    <div className="flex flex-col items-center">
      <WelcomeMessage />
      <Calendar events={MOCK_EVENTS}/>
    </div>
  );
}
