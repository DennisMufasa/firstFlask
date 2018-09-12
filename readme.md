# pre-requisite

<ul>
    <p><strong>Pre-requisite</strong></p>
    <li>Python3-venv</li>
    <li>pip</li>
</ul>

# steps
<ol>
    <li>navigate to the directory containing your app <code>cd dirname</code></li>
    <li>setup a python env <code>python3 -m venv env</code></li>
    <li>set interpreter to your virtual environment <code>ctrl+shift+p (on VS code)</code></li>
    <li>Install flask using pip <code>pip3 install flask</code></li>
    <li>Create an entry point i.e app.py <code>touch app.py</code></li>
    <li>Write routes for endpoints and save</li>
    <li>run the development server<code>python3 -m flask run</code>. The server looks for app.py by default</li>
    <li>add the following after routing<code>if __name__ == "__main__":
                                                app.run(debug=True)
    </code>then run app.py : <code>python app.py</code>
    </li>
    <li>access an endpoint console by on <code>curl IP Address:port</code></li>
    <li>stop the server by: <code>Ctrl+C</code></li>
</ol>