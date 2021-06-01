import React, { useState}  from 'react';
import './Home.css';

function Home(props) {
    const [counter, setCounter] = useState(0);

    const count = () => {
        setCounter(counter+1);
      }

      const post = async () => {
        let user = {counter:counter, hostname:window.location.hostname}
        try {
          //setLoading(true);
          let data = await (await fetch(`/api/post_user_param`, {
            method: 'POST', // *GET, POST, PUT, DELETE, etc.
            mode: 'same-origin', // no-cors, *cors, same-origin
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, *same-origin, omit
            headers: {'Content-Type': 'application/json', 'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value},
            redirect: 'follow', // manual, *follow, error
            referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
            body: JSON.stringify({user:user})
          })).json();
          if (data) {
            console.log(JSON.stringify(data));
          }
        }
        catch(err) {}
        // finally {setLoading(false)}
      };

    return (
        <main className='homePage'>
            <h2>Home Sweeter Home 3</h2>
            <span>Counter:{counter}</span>
            <br/><br/>
            <input type="button" className="btn btn-warning" value="Count" onClick={count} />
            <br />
            <input type="button" className="btn btn-success" value="Post" onClick={post} />
        </main>
      );
    }
export default Home;