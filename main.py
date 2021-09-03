class Hw1Q1:

    def timeConvert(input_seconds):

        input_seconds = 824092835

        day = input_seconds /86400
        hours = input_seconds / 3600
        minutes = input_seconds / 60
        seconds = input_seconds / 1

        return day, 'days', hours, ' hours', minutes, ' minutes', seconds, 'seconds'

    print(timeConvert)