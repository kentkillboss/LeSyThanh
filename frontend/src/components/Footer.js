import React from "react";
import "./Footer.css";

function Footer() {
  return (
    <div className="main-footer">
        <div className="container">
          <div className="row">
            {/* Column1 */}
            <div className="col">
              <h4>Nhóm sinh viên</h4>
              <h3 className="list-unstyled">
                <li>Lê Sỹ Thành</li>
                <li>Tạ Văn Ân</li>
                <li>Đặng Văn Trọng</li>
              </h3>
            </div>
            {/* Column2 */}
            <div className="col">
              <h4>Stuff</h4>
              <ui className="list-unstyled">
                <li>DANK MEMES</li>
                <li>OTHER STUFF</li>
                <li>GUD STUFF</li>
              </ui>
            </div>
            {/* Column3 */}
            <div className="col">
              <h4>Hướng dẫn</h4>
              <ui className="list-unstyled">
                <li>GV.Lê Văn Minh</li>
                <li>Nguyễn Bảo Minh Hoàng</li>
                <li>Nguyễn Đình Trọng</li>
              </ui>
            </div>
            <div className="col">
              <h4>Map</h4>
              <div > 
                <div className="google-map-code">
                    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3834.662526567003!2d108.22282281480729!3d16.03107378890453!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x314219efed0f7bad%3A0x8ef929eb62e2b737!2zNTkgVHLGsMahbmcgQ2jDrSBDxrDGoW5nLCBIb8OgIEPGsOG7nW5nIE5hbSwgSOG6o2kgQ2jDonUsIMSQw6AgTuG6tW5nLCBWaeG7h3QgTmFt!5e0!3m2!1svi!2s!4v1611634232984!5m2!1svi!2s" width="220" height="100%" frameborder="0" style={{border:0}} allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>
                </div>
            </div>
            </div>
          </div>
          <hr />
          <div className="row">
            <p className="col-sm">
              &copy;{new Date().getFullYear()} CÔNG NGHỆ WEB| All rights reserved |
              Terms Of Service | Privacy
            </p>
          </div>
        </div>
      </div>
  );
}

export default Footer;