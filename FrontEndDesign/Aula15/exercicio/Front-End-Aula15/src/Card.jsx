const Card = () => {
    return (
        <div className="w-full max-w-md bg-white shadow-xl rounded-2xl overflow-hidden">
            <img className="w-full h-60 object-cover" src="https://wallpaperaccess.com/full/2992173.jpg" alt="Imagem Ilustrativa"/>
            <div className="p-6 text-center">
                <h2 className="text-2xl font-bold text-gray-900">Toothless</h2>
                <p className="text-gray-600 mt-3"> Furia da noite, um dragão unico.</p>
                <button className="mt-5 w-full py-3 bg-green-500 text-white rounded-lg text-lg font-semibold hover:bg-blue-600 transition duration-300"> Saiba Mais </button>
            </div>
        </div>
    );
};

export default Card;