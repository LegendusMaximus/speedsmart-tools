# speedsmart-tools
A set of tools to help me export my SpeedSmart table

## Reasons

This needs to be created as:
- SpeedSmart for iOS only exports your last 3000 speedtests, and I have more than that. I would like to create a complete table file.
- SpeedSmart will truncate a network name containing the & character, and a program can easily restore those names given a list of what they are
- Network names containing a # symbol are not included in the export (i.e. They have a row but the name comes through as "N/a"). We need to identify these by location/IP and ISP/time/a combination and add them.

## Project parts
- [x] Get back my full length SpeedSmart table
- [ ] Restore the full network names for networks containing & or #
- [ ] Get the Count column back in my new combined table
- [ ] Optional: add average calculation whenever the code runs


## Ideas
- Receive the last 3000 speedtests via email, rather than opening file
- After completion, email back to user
- Calculate averages if the user includes a certain string in the email body (e.g. [[averages=true]])