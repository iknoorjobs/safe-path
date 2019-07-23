import React, { Component } from 'react';
import axios from 'axios';
import '../App.css';
var L = window.L;
var d3 = window.d3;

var data = [];
var heat = [];
var hexLayer = null;

class Directions extends Component {
  state = { mapObj: null, latitude: null, longitude: null };

  generateHexLayer = () => {
    var options = {
      opacity: 0.5,
    };
    hexLayer = L.hexbinLayer(options).addTo(this.state.mapObj);
    hexLayer.colorScale().range(['white', 'red']);

    hexLayer
      .radiusRange([12, 12])
      .lng(function (d) { return d[0]; })
      .lat(function (d) { return d[1]; })
      .colorValue(function (d) { return heat[`${d[0].o[0] + d[0].o[1]}`]; })
      .radiusValue(function (d) { return d.length; });
    hexLayer.data(data);
  }

  renderMap = () => {
    var mymap = L.map('mapid').setView([28.4880472, 77.0653845], 14);
    mymap.options.maxZoom = 15;
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(mymap);
    axios.get('/centres/')
    .then((res) => {
      res.data.map((hexagon) => {
        data.push(hexagon.centre);
        heat[`${hexagon.centre[0] + hexagon.centre[1]}`] = hexagon.heat; 
      });
      data.push([-70, -70]);
      heat[-140] = 10;
      if(hexLayer) {
        hexLayer.data(data);
      }
    })
    this.setState({ mapObj: mymap }, () => {
      this.generateHexLayer();
      // mymap.locate({ setView: true }).on('locationfound', (e) => {
      //   this.setState({ mapObj: mymap, latitude: e.latitude, longitude: e.longitude });
      // });
    });
    let c = 0;
    var control = L.Routing.control({
      router: new L.Routing.google({
        provideRouteAlternatives: true
      }),
      routeWhileDragging: false,
      reverseWaypoints: false,
      useZoomParameter: false,
      showAlternatives: true,
      addWaypoints: false,
      routeLine: (route, i) => {
        let lineColor = ['red', 'orange', 'green'][c % 3];
        c++;
        let line = L.Routing.line(route, {
          styles: [
            {color: 'black', opacity: 0.15, weight: 9},
            {color: 'white', opacity: 0.8, weight: 6},
            {color: lineColor, opacity: 1, weight: 2}
          ]
        })
        return line;
      },
    })
      .addTo(mymap);

    function createButton(label, container) {
      var btn = L.DomUtil.create('button', '', container);
      btn.setAttribute('type', 'button');
      btn.innerHTML = label;
      return btn;
    }

    mymap.on('click', function (e) {
      var container = L.DomUtil.create('div'),
        startBtn = createButton('Start from this location', container),
        destBtn = createButton('Go to this location', container);

      L.popup()
        .setContent(container)
        .setLatLng(e.latlng)
        .openOn(mymap);

      L.DomEvent.on(startBtn, 'click', function () {
        control.spliceWaypoints(0, 1, e.latlng);
        mymap.closePopup();
      });
      L.DomEvent.on(destBtn, 'click', function () {
        control.spliceWaypoints(control.getWaypoints().length - 1, 1, e.latlng);
        mymap.closePopup();
      });
    });


  }

  componentDidMount() {
    this.renderMap();
  }

  render() {
    const { classes } = this.props;

    return (
      <div style={{width: '100%', height: '100%'}}>
        <div id="mapid" style={{width: '100%', height: '100%'}}></div>
      </div>
    );
  }
}

export default Directions;
