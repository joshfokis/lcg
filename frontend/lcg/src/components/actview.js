import ActCard from './act'

export default function ActView(props) {
    return (
        <div>
            {props.act.map(act => <ActCard act={act} />)}
        </div>
    )
}