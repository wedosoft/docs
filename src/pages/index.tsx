import { useEffect } from 'react';
import { useHistory } from '@docusaurus/router';

export default function HomeRedirect() {
    const history = useHistory();
    useEffect(() => {
        history.replace('/intro');
    }, [history]);
    return null;
}
