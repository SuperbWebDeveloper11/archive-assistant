
### archive-assistant    
archive-assistant is a django project built for an office who receive incoming mail and archive it  
  
  
### how office employees will interact with the app:  
- Office employees could login using username and password or create new accounts   
- Create mail instances of each incoming mail  
- Each instance will have : registration number, reference number, source, title, pdf_copy  
- In this case the incoming mail source will be institutes   
- Institutes could only been created by the admin  
- Office employees could filter the incoming mail list based on (registration number, reference number, source, title)  
  
  
### archive-assistant is built using:  
- Django   
- django-crispy-forms  
- django-filter  
- bootstrap  
- JQuery (to perform crud operations without refreshing the page)
  

#### here are some screensshot for the archive-assistant:

- The Entity Relationship Diagram for the project:
![screenshot](https://github.com/pedrasfloki/archive-assistant/blob/main/screenshot%20for%20archive-assistant/archiving%20assistant.png)

- display all incomiing mails along with a filter form:
![screenshot](https://github.com/pedrasfloki/archive-assistant/blob/main/screenshot%20for%20archive-assistant/Screenshot%20from%202021-06-06%2009-39-18.png)

- filter incoming mails by model attributes:
![screenshot](https://github.com/pedrasfloki/archive-assistant/blob/main/screenshot%20for%20archive-assistant/Screenshot%20from%202021-06-06%2009-39-30.png)

- employees should be logged in to perform crud operations:
![screenshot](https://github.com/pedrasfloki/archive-assistant/blob/main/screenshot%20for%20archive-assistant/Screenshot%20from%202021-06-06%2009-39-52.png)

- create instance operation are performed in bootstrap model: 
![screenshot](https://github.com/pedrasfloki/archive-assistant/blob/main/screenshot%20for%20archive-assistant/Screenshot%20from%202021-06-06%2009-40-59.png)

- displaying details instance operation are performed in bootstrap model: 
![screenshot](https://github.com/pedrasfloki/archive-assistant/blob/main/screenshot%20for%20archive-assistant/Screenshot%20from%202021-06-06%2009-41-26.png)

- edit instance operation are performed in bootstrap model: 
![screenshot](https://github.com/pedrasfloki/archive-assistant/blob/main/screenshot%20for%20archive-assistant/Screenshot%20from%202021-06-06%2009-41-32.png)

- delete instance operation are performed in bootstrap model: 
![screenshot](https://github.com/pedrasfloki/archive-assistant/blob/main/screenshot%20for%20archive-assistant/Screenshot%20from%202021-06-06%2009-41-38.png)

- pdf copies for each incoming mail could been downloaded easily by clicking on download button:
![screenshot](https://github.com/pedrasfloki/archive-assistant/blob/main/screenshot%20for%20archive-assistant/Screenshot%20from%202021-06-06%2009-41-54.png)

  
