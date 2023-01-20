import React, { useState } from 'react';
import AuthSection from './AuthSection';
import PreviewSection from './PreviewSection';

import Row from "react-bootstrap/Row"
import Col from "react-bootstrap/Col"

export default function AuthPage(props) {
    return (
        <Row className="w-100 h-100">
            <Col> 
                <PreviewSection></PreviewSection>
            </Col>
            <Col className="d-flex justify-content-center align-items-center">
                <AuthSection setUser = {props.setUser}></AuthSection>
            </Col>
        </Row>
    )
}