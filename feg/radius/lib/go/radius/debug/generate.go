/*
Copyright 2020 The Magma Authors.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

//go:generate go run generate_main.go -o generated.go /usr/share/freeradius/dictionary.rfc2865 /usr/share/freeradius/dictionary.rfc2866 /usr/share/freeradius/dictionary.rfc2867 /usr/share/freeradius/dictionary.rfc2869 /usr/share/freeradius/dictionary.rfc3162 /usr/share/freeradius/dictionary.rfc3576 /usr/share/freeradius/dictionary.rfc5176

package debug
