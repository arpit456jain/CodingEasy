## Directions to add a course

### 1) Add a new Course

1) Create a folder named **newcourse** inside `template/home` folder
2) Create a file newcourse.html
3) Update newcourse.html as per the [template]()
4) Create subfolders named **topic1** inside `template/home/newcourse`
5) Create a file topic1.html
6) Update topic1.html as per the [template]()

### 2) Add a topic to a existing course

1) Create subfolders named **newtopic** inside `template/home/newcourse`
2) Create a file newtopic.html
3) Update newtopic.html as per the [template]()


## Mapping URLS for the added courses/topics

It is the sole responsibility of the contributor to map the added courses. If you are not familiar with Django, you can still use the instructions to map the urls. If you are still unable to do it, kindly mention it in the PR, so someone else will do it.

### 1) Mapping New Course

1) Create a new url for the course. Syntax is provided in [urls.py]() file.
2) Add the new course in the [index.html]() file. Syntax is provided in the file. Do not forget to add the url from step 1 in `index.html` file.
2) Add a view for the new course in [views.py]() file. Syntax is provided in the file.
3) Add a view for the new subtopics [views.py]() file. Syntax is provided in the file.

### 2) Mapping New Topic

1) Add a view for the new subtopics [views.py]() file. Syntax is provided in the file.
