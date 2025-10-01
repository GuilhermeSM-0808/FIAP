// src/App.jsx
import ThreeColumnHero from "./components/ThreeColumnHero.jsx";
import DecoratedText from "./components/DecoratedText.jsx";
import FloatedImageArticle from "./components/FloatedImageArticle.jsx";
import OverlaySVG from "./components/OverlaySVG.jsx";
// import FlexExemplo from "./components/FlexExemplo.jsx";
// import GridExemplo from "./components/GridExemplo.jsx";
import Tipografia from "./components/Tipografia.jsx";
import GalleryHybrid from "./components/GalleryHybrid.jsx";

function App() {
  return (
    <div className="space-y-12">
      <ThreeColumnHero />
      <DecoratedText />
      <FloatedImageArticle />
      <OverlaySVG />
      <Tipografia />
      <GalleryHybrid />
    </div>
  );
}

export default App;