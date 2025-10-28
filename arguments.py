import argparse


days_order = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"]

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--months", nargs="+", help="Lista miesięcy")
    parser.add_argument("--days", nargs="+", help="Lista dni")
    parser.add_argument("--time", nargs="*", help="Pora dnia (domyślnie rano)")
    parser.add_argument("-t", action="store_true", help="Opcja tworzenie")
    parser.add_argument("-o", action="store_true", help="Opcja czytanie z pliku")
    parser.add_argument("-c", action="store_true", help="Opcja czytania plików CSV")

    return parser.parse_args()

def match_short_to_full(short):
    if short == "pn" or short == "pon" or short == "poniedziałek":
        return days_order[0]
    if short == "wt" or short == "wtorek":
        return days_order[1]
    if short == "śr" or short == "sr" or short == "środa":
        return days_order[2]
    if short == "czw" or short == "czwartek":
        return days_order[3]
    if short == "pt" or short == "piątek":
        return days_order[4]
    if short == "sb" or short == "sob" or short == "sobota":
        return days_order[5]
    if short == "nd" or short == "niedz" or short == "niedziela":
        return days_order[6]
    
    

def expand_day_range(day_range):
    if '-' not in day_range:
        return [match_short_to_full(day_range)]
    
    start_short, end_short = day_range.split('-')
    start_full = match_short_to_full(start_short)
    end_full = match_short_to_full(end_short)

    start_idx = days_order.index(start_full)
    end_idx = days_order.index(end_full)

    return days_order[start_idx:end_idx + 1]

def build_schedule(months, days, times):
    schedule = []
    time_index = 0

    for month, day_range in zip(months, days):      
        print(day_range)
        expanded_days = expand_day_range(day_range)
        for day in expanded_days:
            if time_index < len(times):
                t = times[time_index]
            else:
                t = "r"  # domyślnie rano
            time_index += 1

            if t.lower().startswith("r"):
                t_full = "rano" 
            else:
                t_full = "wieczorem"
            schedule.append([month.capitalize(), day, t_full])

    return schedule


if __name__ == "__main__":
    args = parse_args()
    print(args)
    months_list = args.months or []
    days_list = args.days or []
    times_list = args.time or []
    read_flag = args.o 
    create_flag = args.t
    csv_usage_flag = args.c

    schedule = build_schedule(months_list, days_list, times_list)
    
    for row in schedule:
        print(row)