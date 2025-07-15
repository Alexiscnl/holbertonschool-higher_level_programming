def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Invalid template type, expected a string")
        return

    if not isinstance(attendees, list):
        print("Invalid attendees type, expected a list of dictionnaries")
        return

    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Invalid attendee data, expected a dictionary")
            return

    if not template :
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for idx, attendee in enumerate(attendees):
        copy = template
        value_name = attendee.get("name") or "N/A"
        copy = copy.replace("{name}", value_name)

        value_title = attendee.get("event_title") or "N/A"
        copy = copy.replace("{event_title}", value_title)

        value_date = attendee.get("event_date") or "N/A"
        copy = copy.replace("{event_date}", value_date)

        value_location = attendee.get("event_location") or "N/A"
        copy = copy.replace("{event_location}", value_location)

        with open(f"output_{idx + 1}.txt", "w") as f :
            f.write(copy)
