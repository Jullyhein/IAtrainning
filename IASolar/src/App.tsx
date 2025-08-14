import './App.css';
import Logo from './assets/solcabaca.png';          // robô
import Frase from './assets/fraseinicial.png';
import PergunteImg from './assets/pergunte.png';
import FrequenciaImg from './assets/frequencia.png';
import ParaSolarIAImg from './assets/paraSolarIA.png';

import Brand from './assets/solar_group.png';       // ⬅️ logo no canto
import Globo from './assets/globorobo.png';         // ⬅️ esfera na mão

import Hero from '../components/Hero';

export default function App() {
  return (
    <div className="page">
      {/* Logo fixo no canto esquerdo superior */}
      <img src={Brand} alt="Solar Group" className="brand-mark" />

      <header className="hero">
        <Hero
          titleImg={PergunteImg}
          titleSideImg={FrequenciaImg}
          titleBelowImg={ParaSolarIAImg}
          subtitleImg={Frase}
          onAsk={() => alert('Abrir chat')}
        />

        <div className="hero-right">
          {/* Wrap com posição relativa para poder sobrepor o globo */}
          <div className="robot-wrap">
            <img src={Logo} alt="Robô Solar" className="robot" />
            <img src={Globo} alt="" className="robot-globe" />
          </div>
        </div>
      </header>
    </div>
  );
}
