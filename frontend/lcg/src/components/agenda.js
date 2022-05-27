import React from 'react';

function AgendaCard(props) {

    // const imgsrc = "https://arkhamdb.com/" + props.agenda.imgsrc
    return (
        <div>
            {props.agenda.code}
            <img src={"https://arkhamdb.com" + props.agenda.imagesrc} alt="card" />
        </div>
    )
}

export default AgendaCard;