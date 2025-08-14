type Props = {
  titleImg?: string;        // imagem principal do título
  titleSideImg?: string;    // imagem ao lado do título
  titleBelowImg?: string;   // imagem logo abaixo
  subtitleImg?: string;     // subtítulo como imagem
  onAsk?: () => void;
};

export default function Hero({ titleImg, titleSideImg, titleBelowImg, subtitleImg, onAsk }: Props) {
  return (
    <div className="hero-left">
      <div className="title-row">
        {titleImg && <img src={titleImg} alt="Título" className="title-img" />}
        {titleSideImg && <img src={titleSideImg} alt="Frequência" className="title-side-img" />}
      </div>

      {titleBelowImg && (
        <img src={titleBelowImg} alt="Título abaixo" className="title-below-img" />
      )}

      {subtitleImg && (
        <img src={subtitleImg} alt="Frase inicial" className="subtitle-img" />
      )}

      <button className="cta" onClick={onAsk}>Perguntar</button>
    </div>
  );
}
