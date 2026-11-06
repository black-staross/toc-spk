import React from 'react';
import ReactDOM from 'react-dom/client';
import ToeicSpeakingApp from './ToeicSpeakingApp';
import './app.css';

const rootElement = document.getElementById('root');
if (rootElement) {
  ReactDOM.createRoot(rootElement).render(
    <React.StrictMode>
      <ToeicSpeakingApp />
    </React.StrictMode>
  );
}
