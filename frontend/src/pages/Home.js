import React from "react";
import { MDBCarousel, MDBCarouselCaption, MDBCarouselInner, MDBCarouselItem, MDBView, MDBMask, MDBContainer } from
"mdbreact";
import Carousel from 'react-bootstrap/Carousel'

const CarouselPage = () => {
  return (
    <Carousel>
  <Carousel.Item>
    <img
      className="d-block w-100"
      src="https://mdbootstrap.com/img/Photos/Slides/img%20(68).jpg"
      alt="First slide"
    />
    <Carousel.Caption>
      <h3>CÔNG NGHỆ WEB</h3>
      <p>Lớp 17CT1 - Nhóm 3</p>
    </Carousel.Caption>
  </Carousel.Item>
  <Carousel.Item>
    <img
      className="d-block w-100"
      src="https://mdbootstrap.com/img/Photos/Slides/img%20(6).jpg"
      alt="Third slide"
    />

    <Carousel.Caption>
      <h3>LÊ SỸ THÀNH</h3>
      <p>Next</p>
    </Carousel.Caption>
  </Carousel.Item>
  <Carousel.Item>
    <img
      className="d-block w-100"
      src="https://mdbootstrap.com/img/Photos/Slides/img%20(9).jpg"
      alt="Third slide"
    />

    <Carousel.Caption>
      <h3>Tạ Văn Ân</h3>
      <p>Next</p>
    </Carousel.Caption>
  </Carousel.Item>
  <Carousel.Item>
    <img
      className="d-block w-100"
      src="https://mdbootstrap.com/img/Photos/Slides/img%20(70).jpg"
      alt="Third slide"
    />

    <Carousel.Caption>
      <h3>Đặng Văn Trọng</h3>
      <p>Next</p>
    </Carousel.Caption>
  </Carousel.Item>
</Carousel>
  );
}

export default CarouselPage;