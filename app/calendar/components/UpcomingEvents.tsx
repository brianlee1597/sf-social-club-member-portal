import { CalendarEvent } from "./Calendar";

type EventRowProps = {
    event: CalendarEvent;
}

const EventRow = ({ event }: EventRowProps) => {
    return (
        <li className="list-row">
            <div className="text-4xl font-thin opacity-30 tabular-nums">{(new Date(event.startDateTime)).getUTCDate()}</div>
            <div className="list-col-grow">
                <div>{event.name}</div>
                <a className="link text-xs font-semibold opacity-60" href={event.rsvpUrl}>{`RSVP and add to Calendar`}</a>
            </div>
        </li>
    )
}

type UpcomingEventsProps = {
    events: CalendarEvent[];
}

export const UpcomingEvents = ({ events }: UpcomingEventsProps) => {
    return (
        <div>
            <h4 className="text-center">What's Happening?</h4>
            <ul className="list bg-base-100 roundex-box">
                {events.map((event) => (
                    <EventRow key={event.id} event={event}/>
                ))}
            </ul>
        </div>
    )
}