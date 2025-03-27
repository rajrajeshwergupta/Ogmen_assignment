#include <rclcpp/rclcpp.hpp>
#include <sensor_msgs/msg/laser_scan.hpp>
#include <std_msgs/msg/header.hpp>
#include <vector>
#include <chrono>

using namespace std::chrono_literals;

using std::placeholders::_1;

class LaserFilter : public rclcpp::Node {
public:
    LaserFilter(): Node("laser_filter") {
        subscription_ = this->create_subscription<sensor_msgs::msg::LaserScan>("/scan", 10,
            std::bind(&LaserFilter::topic_callback, this, _1)
        );

        publisher_ = this->create_publisher<sensor_msgs::msg::LaserScan>("/filtered_scan", 10);
    }

private:
    void topic_callback(const sensor_msgs::msg::LaserScan::SharedPtr msg) {
        auto filtered_scan = *msg;//sensor_msgs::msg::LaserScan();
        filtered_scan.angle_min = 0.0;
        filtered_scan.angle_max = 2.09; //120

        // Calculate indices for 0 to 120 degrees
        int start_index = ((0 - msg->angle_min) / msg->angle_increment);
        int end_index = ((2.09 - msg->angle_min) / msg->angle_increment);

        start_index = std::max(0, start_index);
        end_index = std::min(static_cast<int>(msg->ranges.size())-1, end_index);

        filtered_scan.ranges  =  std::vector<float>(msg->ranges.begin() + start_index, msg->ranges.begin()+end_index);
        filtered_scan.intensities  =  std::vector<float>(msg->intensities.begin() + start_index, msg->intensities.begin()+end_index);

        publisher_->publish(filtered_scan);
    }
    
    rclcpp::Subscription<sensor_msgs::msg::LaserScan>::SharedPtr subscription_;
    rclcpp::Publisher<sensor_msgs::msg::LaserScan>::SharedPtr publisher_;
};

int main(int argc, char * argv[]) {
    rclcpp::init(argc, argv);
    auto node = std::make_shared<LaserFilter>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}