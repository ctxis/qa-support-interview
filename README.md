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
service outputs the **last successful login for each user on the server**. This output is uploaded to
another service which parses the file.

The upload service can be used only from members of the `Admin` group. The service also has another
group which is called `User`. The file can be one of the following types:

```
CONTENT_TYPES = [
    'text/plain',
    'text/richtext',
    'application/rtf',
    'image/jpeg',
    'image/png',
    'image/gif',
    'application/pdf',
    'application/msword',
    'application/excel',
    'application/vnd.ms-excel',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
]
```

