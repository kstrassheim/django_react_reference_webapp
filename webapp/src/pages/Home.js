import React, { useState, useEffect }  from 'react';
import './Home.css';

function Home(props) {
    const [counter, setCounter] = useState(0);

    const count = () => {
        setCounter(counter+1);
      }
    return (
        <main className='homePage'>
            <h2>Home Sweeter Home</h2>
            <span>Counter:{counter}</span>
            <br/><br/>
            <input type="button" value="Count" onClick={count} />
        </main>
      );
    }
export default Home;