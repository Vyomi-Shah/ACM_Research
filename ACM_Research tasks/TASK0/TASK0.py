# Task 0: Sneaky Log Cleaner
import re
from datetime import datetime

def transform_logs(input_text: str) -> str:

    # TRANSFORMATION 1
    email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    text_after_step1 = re.sub(email_pattern, '[HIDDEN]', input_text)

    timestamp_pattern = r'(\d{2})/(\d{2})/(\d{4}) (\d{2}):(\d{2})'

    def convert_one_timestamp(match):

        day = int(match.group(1))
        month = int(match.group(2))
        year = int(match.group(3))
        hour = int(match.group(4))
        minute = int(match.group(5))

        date_obj = datetime(year, month, day, hour, minute)

        if 11 <= day <= 13:
            suffix = "th"
        elif day % 10 == 1:
            suffix = "st"
        elif day % 10 == 2:
            suffix = "nd"
        elif day % 10 == 3:
            suffix = "rd"
        else:
            suffix = "th"

        month_name = date_obj.strftime("%B")
        time_in_12_hour_format = date_obj.strftime("%I:%M %p")

        if time_in_12_hour_format[0] == "0":
            time_in_12_hour_format = time_in_12_hour_format[1:]

        nice_timestamp = f"{day}{suffix} {month_name} {year}, {time_in_12_hour_format}"

        return nice_timestamp

    text_after_step2 = re.sub(timestamp_pattern, convert_one_timestamp, text_after_step1)

    text_after_step3 = text_after_step2.replace("ERROR", "ERROR You're cooked bro :(")

    return text_after_step3

if __name__ == "__main__":

    sample_log = "User john@mail.com logged in at 23/08/2025 14:05. ERROR session timeout."

    print("ORIGINAL LOG")
    print(sample_log)

    print()

    print("CLEANED LOG")
    print(transform_logs(sample_log))
