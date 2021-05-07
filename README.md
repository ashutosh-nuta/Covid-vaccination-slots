# Find-Covid-vaccination-slots
A python3 script to continously poll for available COVID-19 vaccination slots in India. <br/>
You can schedule a cron job or manually run the script and can leave it running in the background. It will keep on polling for available vaccination slots in the districts you want and print and speak out (sort of an alert if you're doing something else) details for the centres having available slots.

#### Requirements
You'll need to install the pyttsx3 library for text to speech. <br/> Execute
`pip3 install pyttsx3` on the terminal.

#### Usage
`python3 covid_slots.py `

#### Important variables
- AGE_GROUP: 18 or 45
- DISTRICTS: Mapping of Districts to District Id required for the API call. You can just have districts relevant for you. I don't really know if there is a mapping given somewhere, couldn't find one. You can get it for your concerned district using the following:
  - go to https://www.cowin.gov.in/home 
  - open developer tools (F12 in chrome, or right click and inspect)
  - search by district 
  - fill in your district details and search
  - check networks tab in developer tools 
  - check the request being made and get the district_id from the url.
- num_weeks: number of weeks which you want to check the availability for (Since the API returns data for 7 days in one call).
