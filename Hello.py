# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.title("Welcome to Expense Tracker App!👋")
    st.markdown(
      "<p style='color:#00FFAA;font-size:30px;background-color:#e47200'>The Expense Tracker App is a simple to use expenses management which helps you monitor your day to day expenses. With an easy user interface it helps you set monthly budget,track the categories you spent on, and provide this insights through Data and Charts. This app helps you manage your peresonal finances, control overspending helping in giving you a clarity on where you money is spent, helping you make smarter financial decisions.</p>",
      unsafe_allow_html=True
    )

if __name__ == "__main__":
    run()


