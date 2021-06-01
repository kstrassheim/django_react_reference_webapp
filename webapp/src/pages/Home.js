import React, { useState}  from 'react';
import './Home.css';

function Home(props) {
    const [counter, setCounter] = useState(0);

    // consume websocket connection
    const countSocket = new WebSocket(`ws://${window.location.host}/socket/count`);
    countSocket.onmessage = (e) => {
        const ct = parseInt(JSON.parse(e.data)["counter"]);
        // Update counter only on websocket events
        if (ct) setCounter(ct);
    };
    countSocket.onclose = (e) => { console.error('COunt socket closed unexpectedly'); };

    const post = async () => {
      let user = {counter:counter, hostname:window.location.hostname}
      try {
        //setLoading(true);
        const data = await (await fetch(`/api/post_user_param`, {
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

    const count = () => {
      const ct = counter+1
      //setCounter(ct);
      countSocket.send(JSON.stringify({'counter': ct}));
    }

    return (
        <main className='homePage'>
            <h2>Home Sweeter Home 4</h2>
            <span>Counter:{counter}</span>
            <br/><br/>
            <input type="button" className="btn btn-warning" value="Count" onClick={count} />
            <br />
            <input type="button" className="btn btn-success" value="Post" onClick={post} />
        </main>
      );
    }
export default Home;