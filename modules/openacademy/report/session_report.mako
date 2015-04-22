<html>
    <head>
        <style type="text/css">
            ${css}
        </style>
    </head>
    <body>
        % for session in objects:
            <% setLang(session.course_id.responsible_id.lang) %>
            <h1>${session.name|entity}</h1>
            <h2>Course: ${session.course_id.name|entity}</h2>
        % endfor
    </body>
</html>
