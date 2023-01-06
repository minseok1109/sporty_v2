
import SendbirdApp from '@sendbird/uikit-react/App';
import '@sendbird/uikit-react/dist/index.css';
import { useEffect, useState } from "react";
import { useAppContext } from "../../store"
import { jwtDecode } from 'jwt-js-decode';

export default function Chat() {


    const {
        store: { jwtToken },
    } = useAppContext();

    useEffect(() => {
        const header = { Authorization: `JWT ${jwtToken}` };
        const getUserData = () => {
            fetch("http://localhost:8000/accounts/api/user", header)
                .then((response) => response.json())
                .then((json) => console.log(json));

        };
        getUserData();
    }, []);

    const APP_ID = "DB06BA41-2A05-40AE-8E69-BB26D88F20D8";

    return (
        <>
            <div className="App">
                <SendbirdApp
                    // Add the two lines below.
                    appId={APP_ID}// Specify your Sendbird application ID. 
                    userId={jwtToken &&
                        jwtDecode((jwtToken)).payload.username
                    }
                    nickname={jwtToken &&
                        jwtDecode((jwtToken)).payload.username
                    }    // Specify your user ID.
                // nickname={nickname}
                />
            </div>
        </>
    );
}