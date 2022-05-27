import EncounterCard from './encounter'

export default function EncounterView(props) {
    return (
        <div>
            {props.encounter.map(encounter => <EncounterCard encounter={encounter} />)}
        </div>
    )
}