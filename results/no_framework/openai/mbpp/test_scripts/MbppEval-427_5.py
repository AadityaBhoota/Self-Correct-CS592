def change_date_format(dt):
    # Using regular expression to match the date format yyyy-mm-dd
    match = re.match(r'^(\d{4})-(\d{2})-(\d{2})$', dt)
    if match:
        # Rearranging the date format to dd-mm-yyyy
        return f"{match.group(3)}-{match.group(2)}-{match.group(1)}"
    else:
        return "Invalid date format"

# Test cases




def check(candidate):
    assert change_date_format("2026-01-02") == '02-01-2026'
    assert change_date_format("2020-11-13") == '13-11-2020'
    assert change_date_format("2021-04-26") == '26-04-2021'

check(change_date_format)