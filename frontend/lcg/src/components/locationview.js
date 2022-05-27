import LocationCard from './location'

export default function LocationView(props) {
    return (
        <div>
            {props.location.map(location => <LocationCard location={location} />)}
        </div>
    )
}