'use strict';

const e = React.createElement;

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
      return 'Anmeldung wird geprüft.';
    }

    return e(
      'button',
      { onClick: () => this.setState({ liked: true }) },
      'Anmelden'
    );
  }
}
const domContainer = document.querySelector('#Anmeldebutton');
const root = ReactDOM.createRoot(domContainer);
root.render(e(LikeButton));