# Context QA-support exercise

This repository contains the skeleton Django `servers` application that you have been asked to complete.
Below is a description of the problem, and what features you need to implement.

While completing this exercise please be aware that your use of `git` is examined as well as your 
code, so please ensure your history is clean and commit messages are clear and meaningful.
**Please submit your code as a Github fork, or in a format that contains the `.git` directory**.

You may also use any external packages if you feel the need.

**Timing:** We expect this task to take between 2 to 4 hours. It does not have to be fully complete 
to be submitted, and will form part of the discussion in your final interview. Please implement as 
much as you can, but do not feel you have to spend excessive amounts of time working out every minor detail.
Adding comments describing any limitations or mostly-complete portions of the functionality is acceptable.

## Server monitoring

Context has a lot of servers, and successful logins to them are logged to a central service. This 
service outputs the **last successful login for each user on the server**, a sample of which can be [found in 
data/logins.csv](data/logins.csv).

### logins.csv

The logins.CSV is a snapshot of the output of the hypothetical central login service. Unfortunately the
CSV file contains some abnormalities that you need to clean up while processing, which are described below.

The following headers are present in the CSV file:

`server-name,server-ip,username,full-name,contact,login-time`

An example row would be:

`foster-chapman,3.82.209.138,amiller,Alex Taylor,+44(0)0705 97317,2017-06-19`

The `server-name` and/or `contact` column is sometimes missing from rows in the output. You can 
choose to ignore these rows, or attempt to fill in the missing information, as long as you justify 
your choice.

Each login has an individual row in the CSV. **However**, if the user that has logged in has multiple 
items of contact information associated with their account, then there will be multiple rows per login.

For example, "Alex Taylor" has an email address and a phone number. Therefore, a single login attempt 
will have two lines in the CSV file:

```
foster-chapman,3.82.209.138,amiller,Alex Taylor,+44(0)0705 97317,2017-06-19
foster-chapman,3.82.209.138,amiller,Alex Taylor,alex@test.com,2017-06-19
```

The Django application should treat multiple lines like this as a single login attempt. At a minimum, the 
system should store one piece of contact information per user. 

**Bonus points:** If users have multiple contacts, store all values that the CSV provides.

