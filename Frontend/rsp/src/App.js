// import { Button } from 'antd';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { SignIn } from './pages/SignIn.js';
 
function App() {
  return (
    <div className="">
    <Router>
          <Routes>
              <Route path='/' element={<SignIn />} />
          </Routes>
      </Router>
  </div>
  );
}

export default App;
