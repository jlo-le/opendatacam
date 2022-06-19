import React, { PureComponent } from 'react'
import { connect } from 'react-redux';
import dayjs from 'dayjs';
import OpenMoji from '../shared/OpenMoji.js';
import SVG from 'react-inlinesvg';
import { deleteRecording } from '../../statemanagement/app/HistoryStateManagement.js';
import { getCounterColor, getDisplayClasses } from '../../utils/colors.js';
import { COUNTING_AREA_TYPE } from '../../utils/constants.js';
import RecordingDeleteConfirmationModal from '../shared/RecordingDeleteConfirmationModal.js';

class CustomT extends PureComponent {

    constructor(props) {
        super(props);
        this.color = 'black';
        this.width = 'black';
        this.height = 'black';
        this.speed = 'black';
    }


    componentDidMount() {

    }

    componentWillUnmount() {

    }

    renderDateEnd(dateEnd, active = false) {
        if (!active) {
            return dayjs(dateEnd).format('hh:mm a')
        } else {
            return (
                <span className="font-bold" style={{ color: "#FF0000" }}>Ongoing</span>
            )
        }
    }

    render() {

        return (
            <></>
        )
    }
}

export default connect()(CustomT)
