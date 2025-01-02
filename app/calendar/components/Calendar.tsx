import { DayPicker, Modifiers } from "react-day-picker";

export type CalendarEvent = {
    id: string;
    startDateTime: string;
    endDateTime: string;
    name: string;
    rsvpUrl: string;
}

export type CalendarProps = {
    events: CalendarEvent[]
    onDayClick?(day: Date, modifiers: Modifiers): void
}

export const Calendar = ({ events, onDayClick }: CalendarProps) => {
    const handleOnSelect = () => {
        return;
    }

    const datesFromEvents = events.map((event) => (new Date(event.startDateTime)))

    return (
        <>
            <DayPicker
                className="react-day-picker"
                selected={datesFromEvents}
                mode="multiple"
                onSelect={handleOnSelect}
                onDayClick={onDayClick}
            />
        </>
    )
}