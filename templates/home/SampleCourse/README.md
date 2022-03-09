## Directions to add a course

### 1) Add a new Course

1) Create a folder named **newcourse** inside `template/home` folder
2) Create a file newcourse.html
3) Update newcourse.html as per the [template](https://github.com/arpit456jain/CodingEasy/blob/master/templates/home/SampleCourse/samplecourse.html)
4) Create subfolders named **topic1** inside `template/home/newcourse`
5) Create a file topic1.html
6) Update topic1.html as per the [template](https://github.com/arpit456jain/CodingEasy/blob/master/templates/home/SampleCourse/topic1/topic1.html)

### 2) Add a topic to a existing course

1) Create subfolders named **newtopic** inside `template/home/newcourse`
2) Create a file newtopic.html
3) Update newtopic.html as per the [template](https://github.com/arpit456jain/CodingEasy/blob/master/templates/home/SampleCourse/topic1/topic1.html)

<hr>

## Mapping URLS for the added courses/topics

It is the sole responsibility of the contributor to map the added courses. If you are not familiar with Django, you can still use the instructions to map the urls. If you are still unable to do it, kindly mention it in the PR, so someone else will do it.

### 1) Mapping New Course

1) Create a new url for the course. Syntax is provided in [urls.py](https://github.com/arpit456jain/CodingEasy/blob/master/home/urls.py) file.
2) Add the new course crd in the [index.html](https://github.com/arpit456jain/CodingEasy/blob/master/templates/home/index.html) file. Syntax is provided in the file. Do not forget to change the href url from to the url created in step 1.
2) Add a view for the new course in [views.py](https://github.com/arpit456jain/CodingEasy/blob/master/home/views.py) file. Syntax is provided in the file.
3) Add a view for the new subtopics [views.py](https://github.com/arpit456jain/CodingEasy/blob/master/home/views.py) file. Syntax is provided in the file.

### 2) Mapping New Topic

1) Add a view for the new subtopics [views.py](https://github.com/arpit456jain/CodingEasy/blob/master/home/views.py) file. Syntax is provided in the file.
