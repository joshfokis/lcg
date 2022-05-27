import AgendaCard from './agenda'

export default function AgendaView(props) {
    console.log(props)
    return (
        <div>
            {props.agenda.map(agenda => <AgendaCard agenda={agenda} />)}
        </div>
    )
}