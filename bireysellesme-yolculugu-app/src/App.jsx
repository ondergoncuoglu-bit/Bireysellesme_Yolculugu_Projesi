import React from 'react';
import './App.css';
import { ruyalar, makaleler, imgeler } from './data';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Bireyselleşme Yolculuğu: İnteraktif Deneyim</h1>
        <p>Carl Gustav Jung'un öğretileri ışığında kişisel bir keşif.</p>
      </header>
      <nav className="App-nav">
        <ul>
          <li><a href="#ruyalar">Rüyalar</a></li>
          <li><a href="#aktif-imgelem">Aktif İmgelem</a></li>
          <li><a href="#makaleler">Makaleler</a></li>
          <li><a href="#iching">I Ching</a></li>
        </ul>
      </nav>
      <main className="App-main">
        <section id="ruyalar">
          <h2>Rüyalar: Bilinçdışının Mesajları</h2>
          <p>Kişisel rüya günlüklerinden seçmeler ve Jungiyen analizleri.</p>
          <div className="ruya-galeri">
            {ruyalar.map((ruya) => (
              <div key={ruya.id} className="ruya-kart">
                <h3>{ruya.title}</h3>
                {ruya.image && <img src={`./assets/${ruya.image}`} alt={ruya.title} className="ruya-gorsel" />}
                <p><strong>Tarih:</strong> {ruya.date}</p>
                <p><strong>Rüya Metni:</strong> {ruya.dream_text}</p>
                <p><strong>Analiz:</strong> {ruya.analysis_text}</p>
              </div>
            ))}
          </div>
        </section>
        <section id="aktif-imgelem">
          <h2>Aktif İmgelem: İçsel Dünyayla Diyalog</h2>
          <p>Bilinçdışı imgelerle yapılan çalışmalar ve görselleri.</p>
          <div className="imge-galeri">
            {imgeler.map((imge) => (
              <div key={imge.id} className="imge-kart">
                <h3>{imge.title}</h3>
                {imge.image && <img src={`./assets/${imge.image}`} alt={imge.title} className="imge-gorsel" />}
              </div>
            ))}
          </div>
        </section>
        <section id="makaleler">
          <h2>Makaleler: Akademik Derinlik</h2>
          <p>Bireyselleşme ve Jungiyen psikoloji üzerine yazılmış akademik metinler.</p>
          <div className="makale-listesi">
            {makaleler.map((makale) => (
              <div key={makale.id} className="makale-item">
                <h3>{makale.title}</h3>
                <p>{makale.content}</p>
                {makale.file && <a href={`/src/assets/${makale.file}`} target="_blank" rel="noopener noreferrer">Makaleyi Oku</a>}
              </div>
            ))}
          </div>
        </section>
        <section id="iching">
          <h2>I Ching: Kadim Bilgelik Rehberliği</h2>
          <p>Kritik dönemlerde alınan danışmalar ve yorumları.</p>
          {/* I Ching danışmaları ve yorumları buraya dinamik olarak yüklenecek */}
        </section>
      </main>
      <footer className="App-footer">
        <p>&copy; 2025 Bireyselleşme Yolculuğu. Tüm hakları saklıdır.</p>
      </footer>
    </div>
  );
}

export default App;


